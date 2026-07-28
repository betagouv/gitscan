## Changelog : drive-migrator (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la sécurité, notamment avec l'ajout de l'authentification multi-facteurs (MFA) pour Resana et la sécurisation du téléchargement des archives. L'interface utilisateur a été modernisée et des corrections de bugs ont été apportées pour améliorer la stabilité et l'expérience utilisateur. De nouvelles fonctionnalités ont également été ajoutées, comme la génération de données de démonstration et la gestion des comptes utilisateurs en mode restreint.

### Évolutions fonctionnelles
- **Resana :** Ajout du support de l'authentification multi-facteurs (MFA) via un code à usage unique (OTP) lors de la connexion à Keycloak.
- **Téléchargement d'archives :** Sécurisation du lien de téléchargement des archives ZIP.
- **Interface utilisateur :**
    - Nouvelle interface utilisateur pour le tableau de bord (#133).
    - Amélioration de l'interface de partage (#144).
    - Ajout d'un message lorsqu'il n'y a pas de données à afficher (#145).
    - Ajout d'un favicon (#135).
    - Préremplissage et verrouillage du champ email Resana avec le compte Proconnect.
    - Ajout d'une page "compte en attente" pour les nouveaux utilisateurs en mode restreint.
- **Nouvelles fonctionnalités :**
    - Ajout d'un script pour générer des données de démonstration pour le backend de source de type système de fichiers.
    - Possibilité de limiter le nombre de fichiers migrés par espace de travail.
    - Affichage du nombre de fichiers migrés et de l'état de la migration partielle.
    - Ajout de labels aux backends de source.
    - Envoi d'un email de confirmation à la fin de l'export.
- **Mode restreint :** Implémentation d'un mode restreint avec validation administrative des nouveaux comptes utilisateurs.

### Évolutions techniques
- **CI/CD :**
    - Exécution des workflows sur des runners hébergés par GitHub.
    - Ajout de tests de sécurité avec Zizmor.
    - Corrections de configurations et dépendances dans les workflows CI/CD.
- **Backend :**
    - Utilisation de Python 3.14.6.
    - Mise à jour des dépendances Python.
    - Amélioration de la gestion des erreurs lors du rafraîchissement des tokens d'accès Resana.
    - Utilisation de `ruff` pour le formatage du code source.
    - Généralisation de la méthode d'envoi d'emails.
    - Ajout de la récupération des membres de l'espace de travail Resana via le portail PHP.
- **Frontend :**
    - Mise à jour de Lodash et Next.js.
    - Ajout d'une cible `make frontend-lint` pour le linting du frontend.
    - Utilisation du thème DSFR pour l'interface utilisateur.
    - Injection de la variable d'environnement `FRONTEND_THEME` dans le build Docker du frontend.
- **Infrastructure :**
    - Ajout de variables d'environnement pour l'hôte autorisé en production.

### Autres changements
- Mise à jour de la documentation README avec des instructions de démarrage.
- Suppression de Crisp et retour à une interface utilisateur plus simple.
- Suppression de clés inutilisées dans le projet.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour des dépendances GitHub Actions.
- Correction de problèmes liés à l'affichage de la page de défilement bloquée par les styles Cunningham.
- Correction de l'échappement des entités HTML dans les noms Resana.
- Correction d'un bug dans le statut des tâches Resana.
- Ajout d'un paramètre `DRIVE_SHARE_MEMBERS` pour contrôler le partage des membres dans Drive.
