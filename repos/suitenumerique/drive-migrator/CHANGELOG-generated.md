## Changelog : drive-migrator (30 derniers jours, au 29 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité, l'expérience utilisateur et la robustesse de la migration. Des fonctionnalités importantes ont été ajoutées pour la gestion des comptes, l'authentification multifacteur avec Resana, et le contrôle du nombre de fichiers migrés. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- **Authentification Resana :** Ajout du support de l'authentification multifacteur (MFA) avec Resana via un code à usage unique (OTP) envoyé par Keycloak. [#135](https://github.com/suitenumerique/drive-migrator/issues/135)
- **Gestion des comptes :** Introduction d'un mode restreint nécessitant une validation administrative pour les nouveaux comptes, améliorant la sécurité.
- **Limitation de la migration :** Possibilité de limiter le nombre de fichiers migrés par espace de travail, évitant ainsi des migrations trop importantes.
- **Téléchargement d'archives :** Ajout d'une page dédiée au téléchargement sécurisé d'archives de migration authentifiées.
- **Interface utilisateur :** Amélioration de l'interface utilisateur avec de nouveaux éléments visuels (favicon, thème DSFR, mise à jour de la modale de partage) et des messages d'état plus clairs.
- **Données de démonstration :** Ajout d'un script pour générer des données de démonstration pour le backend de source de type système de fichiers.
- **Informations utilisateur :** Inclusion de la liste des utilisateurs partagés dans les exports Drive.

### Évolutions techniques
- **CI/CD :**
    - Exécution des workflows sur des runners GitHub hébergés pour plus de fiabilité.
    - Correction de plusieurs problèmes liés à la configuration des runners auto-hébergés (dépendances manquantes, variables d'environnement).
    - Ajout de tests de sécurité avec Zizmor.
- **Backend :**
    - Utilisation de `ruff` pour le formatage du code source et du backend.
    - Amélioration de la gestion des noms de fichiers et dossiers contenant des caractères spéciaux.
    - Correction d'une erreur dans la gestion du rafraîchissement des tokens d'accès Resana.
    - Généralisation de la gestion de l'envoi d'emails.
- **Frontend :**
    - Mise à jour de certaines dépendances (lodash, next).
    - Injection du thème DSFR dans le build Docker du frontend.

### Autres changements
- Mise à jour de la documentation README avec des instructions de démarrage simplifiées.
- Suppression de clés inutilisées dans le projet.
- Correction de plusieurs problèmes mineurs d'interface utilisateur et de messages d'erreur.
- Mise à jour des dépendances Python et des actions GitHub.
- Correction de problèmes de linting.
