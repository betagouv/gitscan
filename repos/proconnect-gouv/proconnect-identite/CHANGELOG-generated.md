## Changelog : proconnect-identite (30 derniers jours, au 06/11/2026)

### Résumé
Ce mois a été marqué par un renforcement significatif de la sécurité et de la résilience du service. L'introduction de la connexion via des mots de récupération offre une nouvelle méthode de secours pour les utilisateurs. Parallèlement, d'importants travaux ont été menés sur la visibilité technique du système (observabilité) pour permettre une détection plus rapide des erreurs, ainsi que sur la fluidité du parcours utilisateur grâce à une meilleure gestion des redirections et des notifications par email.

### Évolutions fonctionnelles
- **Sécurité et récupération de compte** :
    - Mise en place de la connexion via des mots de récupération (recovery words) avec envoi d'un email de notification lors de l'utilisation de cette méthode [#2285](https://github.com/proconnect-gouv/proconnect-identite/issues/2285).
    - Création d'une section et d'une page dédiées à la gestion des codes de récupération [#2172](https://github.com/proconnect-gouv/proconnect-identite/issues/2172).
- **Notifications et communication** :
    - Envoi d'emails de confirmation lors de la réinitialisation de mot de passe [#2134](https://github.com/proconnect-gouv/proconnect-identite/issues/2134) et lors du départ d'un utilisateur d'une organisation [#2135](https://github.com/proconnect-gouv/proconnect-identite/issues/2135).
- **Améliorations de l'expérience utilisateur** :
    - Optimisation des parcours de redirection pour éviter les pages d'erreur lors de processus interrompus (annulation de modération, échec de certification, retour FranceConnect, etc.).
    - Correction de la détection des domaines d'emails gratuits [#2246](https://github.com/proconnect-gouv/proconnect-identite/issues/2246).
    - Amélioration de la gestion des choix d'emails de mairie lorsqu'une option est sautée ou inconnue [#2252](https://github.com/proconnect-gouv/proconnect-identite/issues/2252).

### Évolutions techniques
- **Observabilité et traçabilité** :
    - Refonte majeure du système de logs : passage au format JSON et intégration de standards OpenTelemetry pour un meilleur suivi des requêtes (ajout de `trace_id` sur chaque ligne) [#2344](https://github.com/proconnect-gouv/proconnect-identite/issues/2344), [#2353](https://github.com/proconnect-gouv/proconnect-identite/issues/2353), [#2358](https://github.com/proconnect-gouv/proconnect-identite/issues/2358).
    - Amélioration du suivi d'erreurs avec Sentry : séparation des environnements, protection des données sensibles (codes OAuth) dans les traces et meilleure gestion des traces locales [#2352](https://github.com/proconnect-gouv/proconnect-identite/issues/2352), [#2355](https://github.com/proconnect-gouv/proconnect-identite/issues/2355), [#2356](https://github.com/proconnect-gouv/proconnect-identite/issues/2356).
    - Journalisation accrue des activités critiques (changements de mot de passe, modifications de profil, vérifications de domaine, etc.) [#2407](https://github.com/proconnect-gouv/proconnect-identite/issues/2407), [#2408](https://github.com/proconnect-gouv/proconnect-identite/issues/2408), [#2369](https://github.com/proconnect-gouv/proconnect-identite/issues/2369).
- **Gestion du système (Runtime & Data)** :
    - Extension des capacités de gestion via le runtime : gestion des membres, réinitialisation du MFA, modération, suppression de compte et liaison d'identités FranceConnect [#2384](https://github.com/proconnect-gouv/proconnect-identite/issues/2384), [#2386](https://github.com/proconnect-gouv/proconnect-identite/issues/2386), [#2387](https://github.com/proconnect-gouv/proconnect-identite/issues/2387), [#2389](https://github.com/proconnect-gouv/proconnect-identite/issues/2389), [#2390](https://github.com/proconnect-gouv/proconnect-identite/issues/2390), [#2391](https://github.com/proconnect-gouv/proconnect-identite/issues/2391), [#2392](https://github.com/proconnect-gouv/proconnect-identite/issues/2392).
    - Migration des suggestions d'organisations vers Drizzle ORM [#2396](https://github.com/proconnect-gouv/proconnect-identite/issues/2396).
- **Infrastructure et CI/CD** :
    - Optimisation des builds Docker via la mise en place de caches pour les dépendances npm [#2349](https://github.com/proconnect-gouv/proconnect-identite/issues/2349), [#2350](https://github.com/proconnect-gouv/proconnect-identite/issues/2350).
    - Renforcement de la sécurité des workflows GitHub en limitant les permissions des tokens [#2312](https://github.com/proconnect-gouv/proconnect-identite/issues/2312).
    - Auto-hébergement du conteneur Matomo Tag Manager [#2286](https://github.com/proconnect-gouv/proconnect-identite/issues/2286).

### Autres changements
- **Maintenance et données** :
    - Synchronisation régulière de la liste des administrations via Grist [#2427](https://github.com/proconnect-gouv/proconnect-identite/issues/2427), [#2364](https://github.com/proconnect-gouv/proconnect-identite/issues/2364).
    - Nettoyage de la liste de mots Diceware pour retirer les termes offensants ou sensibles [#2266](https://github.com/proconnect-gouv/proconnect-identite/issues/2266).
