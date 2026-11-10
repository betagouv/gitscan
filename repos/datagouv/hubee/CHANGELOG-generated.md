## Changelog : hubee (30 derniers jours, au 09/11/2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'expérience utilisateur sur le portail, notamment via une meilleure gestion des agents et des abonnements. L'API a gagné en robustesse avec de nouvelles fonctionnalités de gestion des membres et une gestion des erreurs plus explicite. Parallèlement, un effort important a été porté sur la sécurité, la conformité du design (DSFR) et la qualité de la journalisation des activités.

### Évolutions fonctionnelles
- **Gestion des agents et des organisations** : 
    - Possibilité de lister les agents d'une organisation et de consulter leurs détails (champs de profil, date de dernière connexion).
    - Amélioration de l'affichage : les agents sont désormais nommés par leur nom de famille en priorité et les flux sont affichés sous forme de tags.
    - Les flux sont désormais identifiables par leur nom plutôt que par leur code technique.
    - Ajout du numéro de téléphone mobile dans les informations de contact.
- **Gestion des abonnements** : Ajout de la possibilité de lister et de consulter le détail des abonnements d'une structure.
- **Évolutions de l'API** :
    - Nouvelles capacités pour l'enregistrement, la validation et la vérification des droits des agents.
    - Amélioration de la gestion des erreurs : l'API répond désormais systématiquement en JSON avec un code et un message explicite, même pour les routes inconnues (404).
    - Meilleure gestion des codes de flux (vérification de l'existence et de la casse).
- **Interface et Ergonomie** :
    - Mise en conformité des pages d'erreur avec le design système DSFR.
    - Ajout d'un accès direct aux télédossiers via le menu.
- **Audit** : Ouverture de l'accès au journal des traces d'audit.

### Évolutions techniques
- **Sécurité et Infrastructure** :
    - Correction de plusieurs vulnérabilités (CVE) sur les dépendances.
    - Mise à jour de l'environnement vers Ruby 4.0.9.
    - Sécurisation des conteneurs Docker via l'utilisation d'images "distroless" en mode non-root.
    - Nettoyage du magasin TLS (retrait de racines compromises).
- **Journalisation (Logs)** : Refonte majeure pour améliorer la traçabilité et la confidentialité :
    - Inclusion de l'adresse IP de l'appelant sur chaque ligne de requête.
    - Masquage des données sensibles (nonces et adresses ProConnect, noms de fichiers de pièces jointes).
    - Amélioration de la lisibilité des logs (regroupement des exceptions et des redirections sur une seule ligne).
- **Architecture API** : Mise en place du versionnement de l'API par le chemin d'URL et renforcement de la lecture des jetons d'authentification (via l'en-tête Authorization uniquement).
- **Maintenance et Performance** :
    - Automatisation de la purge quotidienne des traces d'audit de plus d'un an.
    - Fiabilisation de la gestion des tâches de fond (jobs) et de leur historique.

### Autres changements
- **Documentation** : Mise à jour de la documentation de l'API (processus d'enregistrement, versionnement) et des événements (schémas et règles d'archivage).
- **Configuration** : Ajout de scripts de préparation (seeds) pour faciliter l'administration locale et les tests.
