# passage-ui

Petite app desktop (Wails : Go + Svelte 5) au-dessus de [passage](https://github.com/FiloSottile/passage) pour gérer des secrets partagés entre admins. Elle tourne en local sur chaque poste.

- Parcourir, rechercher, déverrouiller et copier les secrets (le presse-papier s'efface automatiquement)
- Chaque secret a un **mot de passe**, un **identifiant** (e-mail ou nom d'utilisateur), une **URL** (bouton « Ouvrir » vers le navigateur), une **clé OTP** et des **notes**
- **Codes OTP (TOTP)** : la clé est chiffrée avec age comme le reste. L'app affiche le code à 6 chiffres et le temps restant.
- Créer, modifier, déplacer et supprimer des secrets, avec un générateur de mots de passe
- **Gérer les admins** d'un dossier (`.age-recipients`) : ajout ou retrait d'une clé, puis rechiffrement automatique. Après le retrait d'un admin, l'app liste les secrets à faire tourner.
- Synchronisation git : pull avant chaque écriture, push après
- **Identités protégées par passphrase et YubiKey** : les invites d'age s'affichent dans une boîte de dialogue de l'app

Aucun port réseau n'est ouvert : le front parle au Go via le pont IPC de la webview.

Le thème s'inspire du DSFR : police Marianne (embarquée dans `frontend/src/fonts/`, tirée de `@gouvfr/dsfr` 1.14), tokens de couleur DSFR en clair et en sombre (suit le thème du système), boutons, champs, badges, tags et alertes façon `fr-*`. Seuls les tokens et les polices sont repris : l'app n'utilise pas le CSS du DSFR, pour rester légère et hors ligne. Il n'y a pas de bloc marque « République française ». **Marianne est réservée aux services de l'État** (CGU du DSFR) : si l'outil sort de ce cadre, il faut retirer les `@font-face` en tête de `style.css`.

## Prérequis (sur chaque poste admin)

- Linux ou macOS (passage est un script bash, et l'app utilise un pseudo-terminal)
- `passage`, `age` ≥ 1.1, `git`, et `age-plugin-yubikey` pour les YubiKeys
- Pour compiler : Go ≥ 1.26.6 (corrige deux CVE de la bibliothèque standard ; le `toolchain` est épinglé dans `go.mod`), Node ≥ 20, et la CLI Wails : `go install github.com/wailsapp/wails/v2/cmd/wails@latest` (puis `wails doctor` pour vérifier les dépendances système, par ex. webkit2gtk sous Linux)

## Lancer

```sh
go mod tidy          # génère go.sum
wails dev            # mode dev avec rechargement à chaud
wails build          # binaire dans build/bin/
```

**Ubuntu 24.04+ / Debian 13+** : seule WebKitGTK 4.1 est disponible. Il faut installer `libwebkit2gtk-4.1-dev` et ajouter `-tags webkit2_41` à chaque commande (`wails dev -tags webkit2_41`, `wails build -tags webkit2_41`). `wails doctor` affiche quand même « libwebkit Not Found », car il ne cherche que la 4.0 : on peut l'ignorer.

`wails dev` / `wails build` génèrent `frontend/wailsjs/` (les bindings JS des méthodes de `App`). Ce dossier est ignoré par git.

Tests du cœur (intégration réelle avec age, passage et git, sans Wails) :

```sh
go test ./internal/...
```

## Format d'un secret

On garde la convention de pass/passage, que comprennent aussi la CLI, browserpass, passff et pass-otp :

```
Xk7#pQ2!vLm9@wR4zT8e                                       ← ligne 1 : mot de passe
login: ops@exemple.gouv.fr                                 ← identifiant
url: https://console.clever-cloud.com                      ← adresse du service
otpauth://totp/Clever%20Cloud:ops@…?secret=JBSW…&issuer=…  ← clé OTP
codes de secours : …                                       ← notes libres
```

- À la lecture, `login:`, `username:`, `user:`, `email:`, `e-mail:` et `identifiant:` sont reconnus, ainsi que `url:`, `link:`, `website:` et `site:`. L'app réécrit ensuite en `login:` et `url:`. Seule la ligne 1 a une place imposée.
- L'URL est normalisée (`console.exemple.fr` devient `https://console.exemple.fr`). Seul `http(s)` est accepté, à l'enregistrement comme à l'ouverture : un fichier écrit en CLI ne peut pas faire ouvrir un `file://` ou un `javascript:`.
- Dans l'éditeur, la clé OTP s'accepte sous forme d'URI `otpauth://totp/…` (celle du QR code) ou de clé base32 seule (le « code de saisie manuelle » des services, espaces acceptés). Elle est normalisée en URI. Un aperçu du code courant permet de valider la clé au moment d'activer la 2FA.
- Algorithmes gérés : SHA1, SHA256 et SHA512, avec 6 à 8 chiffres et une période configurable. HOTP n'est pas géré.
- `passage show nom` affiche toujours tout le fichier. `passage show -c nom` copie toujours la ligne 1.

Point à garder en tête : mettre le mot de passe et la clé OTP dans le même fichier fait des deux facteurs un seul secret pour qui peut le déchiffrer. C'est le choix de pass-otp et de la plupart des gestionnaires d'équipe. Si vous voulez vraiment séparer les deux facteurs, rangez les clés OTP dans un sous-dossier chiffré pour d'autres admins.

## Architecture

```
main.go                     démarrage Wails
app.go                      méthodes exposées au front + invites + presse-papier
unlock.go                   déverrouillage temporaire, copie par champ, codes OTP
internal/passage/
  runner.go                 exécution de passage/age/git dans un pty (voir plus bas)
  store.go                  liste, show, insert, rm, mv, reencrypt, générateur
  recipients.go             lecture/écriture/validation des .age-recipients
  git.go                    statut, pull --rebase, push, commit
  secret.go                 champs ⇄ format pass (mot de passe, login, otpauth, notes)
  totp.go                   TOTP RFC 6238 (testé sur les vecteurs de la RFC)
frontend/src/
  App.svelte                layout, événements Go, file d'invites, toasts
  lib/Tree.svelte           arbre du store
  lib/SecretView.svelte     déverrouiller, champs, copier, modifier, déplacer, supprimer
  lib/OtpCode.svelte        code OTP + compte à rebours
  lib/Editor.svelte         création et édition par champs, générateur, aperçu OTP
  lib/Admins.svelte         gestion des admins d'un dossier
  lib/PromptDialog.svelte   saisie passphrase / PIN
  lib/Settings.svelte       chemins, délais, auto-sync
```

### Passphrase et YubiKey : le pseudo-terminal

age ne lit jamais la passphrase d'une identité (ni le PIN d'une YubiKey) sur stdin, mais sur `/dev/tty`. Chaque commande est donc lancée dans une nouvelle session dont le **terminal de contrôle est un pty détenu par l'app** (`Setsid` + `Setctty`) :

- ce qu'age écrit sur le pty est une invite ; l'app l'envoie au front (événement `prompt`), qui renvoie la réponse (`AnswerPrompt`), écrite ensuite sur le pty ;
- stdout (le secret) et stderr restent des pipes séparés, donc **le secret ne passe jamais par le pty** ;
- stderr est relayé en notifications. C'est par là qu'`age-plugin-yubikey` affiche « touch your YubiKey », que l'UI met en avant.
- Si l'utilisateur annule, le process est tué.

`passage reencrypt` appelle age une fois par fichier. La réponse à une invite est donc **gardée le temps d'une seule opération** (puis effacée), pour ne pas redemander la passphrase à chaque fichier. En dehors du déverrouillage d'un secret (voir ci-dessous), rien n'est mis en cache.

Le même mécanisme couvre git sur SSH avec une clé protégée par passphrase, mais un `ssh-agent` reste plus confortable.

## Sécurité : ce que l'app fait et ne fait pas

- **Déverrouiller** déchiffre le secret une fois et garde ses champs **en mémoire côté Go** pendant N secondes (Réglages, 60 s par défaut), puis les efface. Un seul secret est déverrouillé à la fois, et on le reverrouille en changeant de secret ou avec « Verrouiller maintenant ». Sans ce mécanisme, afficher un code OTP qui change toutes les 30 s obligerait à redemander la passphrase ou la YubiKey à chaque période.
- La **clé OTP ne quitte jamais le Go** : le front reçoit seulement le code courant, sauf dans l'éditeur, qui en a besoin pour la modifier. Le **mot de passe** et les **notes** ne vont au front que sur « Afficher ».
- **Copier** (mot de passe, identifiant, code OTP) passe par le Go. Le presse-papier est vidé après N secondes, sauf si son contenu a changé entre-temps.
- Les buffers Go sont mis à zéro après usage. Les chaînes Go et JS ne peuvent pas l'être, donc un secret affiché reste en mémoire jusqu'au passage du GC. C'est acceptable pour un poste admin, mais ce n'est pas un coffre matériel.
- **Retirer un admin ne révoque rien rétroactivement.** Il garde les anciennes versions chiffrées pour lui dans l'historique git et dans son clone. L'app le rappelle et liste les secrets du dossier à changer.
- Les noms de secrets sont validés (pas de `..`, pas de chemin absolu, pas de fichier caché) avant d'être passés à passage.
- **Le store est partagé par git : on ne fait pas confiance à son contenu.** Avant toute lecture ou écriture, le chemin visé est résolu sur le disque et tout composant qui est un lien symbolique est refusé (`ResolveStorePath`), et un rechiffrement refuse un sous-arbre contenant le moindre lien. Sans cela, un co-admin pourrait committer un `secret.age` ou un `.age-recipients` en lien symbolique vers, par ex., `~/.ssh/authorized_keys` : après `git pull`, `os.WriteFile` et `age -o` écriraient à travers ce lien, hors du store. `List` ignore de même les secrets qui sont des liens symboliques.
- Toute nouvelle liste d'admins est validée par age (`age -e -r …`) avant d'être écrite. Une clé `age1yubikey1…` demande donc que le plugin soit installé.

## Limites connues / pistes

- La détection des invites est heuristique (une ligne qui finit par `:` ou `?`, ou qui contient passphrase / PIN) et repose sur `LC_ALL=C`. Elle est testée avec une identité à passphrase, **pas encore avec une vraie YubiKey** : c'est le premier test à faire.
- Une invite sans réponse expire au bout de 5 min.
- Pas de support Windows (pty et passage).
- Pistes : un cache optionnel de la passphrase pour N minutes (façon gpg-agent), l'historique git d'un secret, le QR code, un bouton « faire tourner » qui génère et enregistre le nouveau mot de passe en un clic, et l'onboarding d'un nouvel admin (générer sa clé et l'ajouter à `.age-recipients`).
