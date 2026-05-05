## Changelog : service-national-universel (30 derniers jours, au 10 mai 2024)

### Résumé
Ce changelog couvre les dernières améliorations apportées à la plateforme du Service National Universel. Les mises à jour se concentrent principalement sur la sécurité, avec des corrections pour la gestion des mots de passe et la protection contre les vulnérabilités, ainsi que sur la résolution de bugs signalés par les utilisateurs et l'équipe de développement.

### Évolutions fonctionnelles
*   **API:** Amélioration de la génération des convocations en utilisant des données communes sur les jeunes. [#3838](https://github.com/betagouv/service-national-universel/issues/3838)
*   **Admin:** Correction de l'affichage de la barre de défilement dans le menu. [#3823](https://github.com/betagouv/service-national-universel/issues/3823)
*   **Admin:** Correction du composant de message d'information et de la gestion des filtres vides. [#3830](https://github.com/betagouv/service-national-universel/issues/3830)

### Évolutions techniques
*   **Sécurité:** Mise à jour de la librairie Mongoose en version 7.8.3 et alignement des dépendances pour corriger une vulnérabilité CVE liée à l'utilisation de `$where`. [#5267](https://github.com/betagouv/service-national-universel/issues/5267)
*   **Sécurité:** Implémentation de la gestion de la variable d'environnement `JWT_SECRET` dans la configuration de l'API et ajout de tests associés. [#5263](https://github.com/betagouv/service-national-universel/issues/5263)
*   **Sécurité:** Blocage de la connexion pour les utilisateurs sans mot de passe. [#5264](https://github.com/betagouv/service-national-universel/issues/5264)
*   **Sécurité:** Hachage des tokens de réinitialisation de mot de passe avec HMAC. [#5265](https://github.com/betagouv/service-national-universel/issues/5265)
*   **API:** Correction de bugs liés aux exports DSNJ et à la cohérence des cohortes. [#3839](https://github.com/betagouv/service-national-universel/issues/3839), [#3849](https://github.com/betagouv/service-national-universel/issues/3849)

### Autres changements
*   **Sentry:** Corrections diverses pour améliorer la robustesse et la gestion des erreurs dans l'interface d'administration (PDT bus validation, dashboard todo, head center session). [#3842](https://github.com/betagouv/service-national-universel/issues/3842), [#3843](https://github.com/betagouv/service-national-universel/issues/3843), [#3835](https://github.com/betagouv/service-national-universel/issues/3835)
*   **Sentry:** Correction d'un cas où l'heure de la réunion était nulle. [#3840](https://github.com/betagouv/service-national-universel/issues/3840)
*   **API:** Amélioration de la gestion des types MIME inconnus lors de l'importation de fichiers. [#3825](https://github.com/betagouv/service-national-universel/issues/3825)
*   **API:** Suppression de la récupération du service départemental pour le modèle de convocation.
