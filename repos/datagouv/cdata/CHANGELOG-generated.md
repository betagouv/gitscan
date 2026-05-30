## Changelog : cdata (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les améliorations apportées à cdata se concentrent sur l'expérience utilisateur, notamment en améliorant la recherche, l'accessibilité et la gestion des utilisateurs. Des fonctionnalités ont été ajoutées pour faciliter l'administration du site, comme la rotation des mots de passe et la gestion des notifications. Des optimisations techniques ont également été réalisées pour améliorer la performance et la maintenance du code.

### Évolutions fonctionnelles
- **Recherche :**
    - Amélioration de la recherche avec des filtres personnalisés plus précis et une meilleure gestion des résultats [#1062, #1067].
    - Correction d'un bug empêchant la réinitialisation de la recherche après une requête [#1089].
    - Annonce du nombre de résultats de recherche pour une meilleure accessibilité [#1096].
- **Administration :**
    - Possibilité de faire pivoter le mot de passe des utilisateurs en tant qu'administrateur [#1078].
    - Ajout de nouvelles notifications pour les administrateurs [#1076].
    - Correction d'un bug dans la recherche d'utilisateurs en administration [#1089].
    - Réintroduction du lien entre les réutilisations et les sujets [#1082].
- **Authentification :**
    - Amélioration de l'utilisation des codes QR pour l'authentification à deux facteurs [#1090].
    - Correction de l'envoi des identifiants avec la nouvelle politique CORS [#1098].
- **Données & Affichage :**
    - Ajout de données sénatoriales aux élections [#1091].
    - Amélioration de l'affichage des contacts [#1075].
    - Ajout d'un segment tabulaire [#1072].
    - Amélioration du SEO (Search Engine Optimization) [#1066].
- **Divers :**
    - Possibilité de définir le titre des cartes [#1092].
    - Correction de liens vers les guides [#1077].
    - Affichage des callbacks en attente et ajout d'un sujet utilisateur [#1073].

### Évolutions techniques
- Mise à jour de la bibliothèque `geopf-extensions-openlayers` vers la version 1.0.0-beta.10 [#1085].
- Optimisation des dépendances pour améliorer la performance [#1086].
- Mise à jour des dépendances du projet [#1060].
- Passage à Nuxt 4 et mise à jour de la documentation README correspondante [#1068].
- Ajout d'un timestamp dans les logs pour faciliter le débogage [#1084].
- Suppression des effets de bord dans certains composants [#1079, #1080].
- Amélioration de la gestion des erreurs CORS [#1098].

### Autres changements
- Affichage de l'API Swagger [#1055].
- Correction de redirections brisées dans la configuration [#1065].
- Ajout d'une preuve de concept de visualisation (viz poc 1) [#963].
- Ignorer le répertoire du cache pnpm local pour une meilleure gestion de l'espace disque [#1071].
