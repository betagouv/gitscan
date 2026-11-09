## Changelog : le-marche (30 derniers jours, au 08 novembre 2026)

### Résumé
Cette période a été principalement consacrée à un renforcement massif de la sécurité et de la protection des données de la plateforme. Les développements se sont concentrés sur la correction de vulnérabilités, la sécurisation des accès (authentification et API) et l'amélioration de la confidentialité des informations des structures (SIAE). Parallèlement, une mise à jour importante du système de gestion de contenu (CMS) a été effectuée pour assurer la pérennité technique du projet.

### Évolutions fonctionnelles
- **Gestion des structures (SIAE)** : Les utilisateurs SIAE peuvent désormais être invités à ajouter leur structure une fois que leur adresse a été confirmée.
- **Confidentialité et protection des données** :
    - Masquage automatique des coordonnées de contact pour les SIAE inactives ou radiées.
    - Sécurisation des exports de données (CSV/XLSX) par la neutralisation des formules de feuilles de calcul pour éviter les injections.
    - Amélioration de l'anonymisation des adresses email.
- **Expérience utilisateur et métier** :
    - **Contrôle des accès** : Restriction des données visibles (filtres d'achat, réponses des prestataires, listes de favoris) pour que les utilisateurs ne voient que les informations liées à leur propre entreprise ou leurs appels d'offres.
    - **Notifications** : Optimisation des rappels d'appels d'offres et des notifications de groupements pour éviter les envois redondants.
    - **Navigation** : Amélioration de la clarté du plan du site.

### Évolutions techniques
- **Sécurité et Authentification** (Priorité haute) :
    - Correction de vulnérabilités critiques, notamment contre les injections XSS et les failles de type IDOR (accès non autorisé à des ressources tierces).
    - Renforcement de la protection contre l'énumération d'utilisateurs lors de l'inscription et sécurisation de la gestion des jetons (tokens) API.
    - Masquage des secrets d'authentification dans les journaux (logs) et durcissement des politiques d'upload sur S3.
    - Sécurisation de la gestion des emails (vérification de l'expéditeur et durcissement des alias de réponse).
- **Maintenance du CMS (Wagtail & Sites-Conformes)** :
    - Migration et adaptation majeure du système de gestion de contenu vers les nouvelles versions de `sites-conformes`.
    - Mise à jour des composants de design (Django-DSFR) et nettoyage des templates.
    - Optimisation de la gestion du sitemap et des renditions d'images.
- **Infrastructure et Backend** :
    - Amélioration de la stabilité de la connexion Redis.
    - Optimisation des tâches de nettoyage automatique (utilisateurs et appels d'offres obsolètes) et des mises à jour de compteurs.
    - Correction des tâches asynchrones (Huey) et des notifications Slack.

### Autres changements
- Nettoyage du dépôt : suppression de fichiers inutilisés (CleverCloud) et de dépendances obsolètes.
- Réorganisation de fichiers de configuration (cronjson).
