## Changelog : sylvasan (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à SylvaSan au cours du dernier mois. Les développements se concentrent sur l'amélioration de l'expérience utilisateur avec l'ajout de pages légales (mentions légales, données personnelles, cookies), l'intégration de Matomo pour l'analyse, et des corrections de bugs. Des améliorations techniques importantes ont également été réalisées, notamment la mise en place d'un CI/CD, la mise à jour des dépendances et la structuration du projet pour faciliter le déploiement et la maintenance. L'application mobile a également bénéficié de l'ajout de TailwindCSS et DSFR, ainsi que d'une première compilation Android.

### Évolutions fonctionnelles
- Ajout de la page « mentions légales » [#52](https://github.com/betagouv/sylvasan/issues/52).
- Ajout de la page des données personnelles [#4](https://github.com/betagouv/sylvasan/issues/4).
- Ajout de la page « cookies » [#48](https://github.com/betagouv/sylvasan/issues/48).
- Ajout de la déclaration d'accessibilité [#51](https://github.com/betagouv/sylvasan/issues/51).
- Mise à jour du texte de la page d'accueil [#12](https://github.com/betagouv/sylvasan/issues/12).
- Intégration de Matomo pour l'analyse des données d'utilisation [#60](https://github.com/betagouv/sylvasan/issues/60).
- Améliorations UI sur la page de login [#57](https://github.com/betagouv/sylvasan/issues/57).
- Reformulation de la page 404 [#55](https://github.com/betagouv/sylvasan/issues/55).
- Ajout d'un système de notification.
- Mise en place de l'authentification et du routage de base sur l'application mobile.

### Évolutions techniques
- Mise en place d'un CI/CD avec GitHub Actions [#14](https://github.com/betagouv/sylvasan/issues/14).
- Ajout de la licence MIT au projet [#54](https://github.com/betagouv/sylvasan/issues/54).
- Mise à jour de nombreuses dépendances (tailwindcss, vue, capacitor, django, etc.).
- Ajout de tests pour l'application mobile [#39](https://github.com/betagouv/sylvasan/issues/39).
- Première compilation Android de l'application mobile.
- Utilisation de `useTitle` et d'un endpoint pour le token CSRF.
- Ajout de routage basé sur des fichiers.
- Refactoring du code pour utiliser le store d'authentification et renommer la fonction `custom fetch`.
- Ajout de fonctions de thème.
- Utilisation de l'authentification par token sur l'application mobile.
- Déplacement du backend vers une plateforme et ajout d'une nouvelle interface utilisateur sur le frontend web.
- Suppression temporaire des paramètres liés à l'email.
- Ajout de l'ADR 0001.

### Autres changements
- Correction de coquilles.
- Ajout de fichiers `.htaccess` pour le déploiement web.
- Placement des fichiers statiques à l'intérieur de `src`.
- Ajout de TailwindCSS et DSFR pour l'application mobile.
- Ajout de la gestion des erreurs avec un retry automatique pour les requêtes échouées.
- Mise à jour du fichier `README.md`.
- Correction des routes de l'application mobile.
- Ajout de variables d'environnement pour le CI/CD.
- Ajout de fichiers `.yml` pour les workflows GitHub Actions.
- Amélioration du scroll vers le haut d'une page lors d'un changement de route [#50](https://github.com/betagouv/sylvasan/issues/50).
- Suppression de l'utilisation dépréciée de `next` dans `vue-router` [#55](https://github.com/betagouv/sylvasan/issues/55).
- Ajout d'une route 404 [#55](https://github.com/betagouv/sylvasan/issues/55).
