## Changelog : cdata (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, cdata a bénéficié d'améliorations significatives en termes de recherche, d'administration et d'expérience utilisateur. La plateforme a été mise à jour vers Nuxt 4.4 et 4.3, apportant des optimisations de performance et de nouvelles fonctionnalités. Des améliorations ont également été apportées à la gestion des organisations, des notifications et de la visualisation des données.

### Évolutions fonctionnelles
- **Recherche :**
    - Amélioration des filtres personnalisés dans la recherche, avec la possibilité de configurer des placeholders et d'exporter des types pour une meilleure flexibilité [#1067, #1062, #1064, #1049].
    - Correction d'un bug où la recherche ne réinitialisait pas la page [#1089].
    - Correction d'un bug où le flash de recherche ne disparaissait pas après réinitialisation [#1083].
- **Administration :**
    - Possibilité de faire pivoter les mots de passe des utilisateurs dans l'interface d'administration [#1078].
    - Réintroduction du lien entre les jeux de données et les sujets [#1082].
    - Amélioration de l'affichage des contacts [#1075].
    - Ajout de nouvelles notifications pour les administrateurs [#1076].
- **Organisations :**
    - Nouvelle mise en page pour les pages d'organisations [#1051].
    - Affichage des activités pour les membres des organisations [#1052].
- **Autres améliorations :**
    - Ajout d'une section tabulaire [#1072].
    - Ajout de données sénatoriales aux élections [#1091].
    - Amélioration des textes d'aide pour l'URL de base de l'API [#1093].
    - Correction de liens brisés dans la configuration [#1065].
    - Amélioration du SEO [#1066].
    - Affichage de Swagger [#1055].
    - Correction de l'affichage des guides et liens vers le score de qualité [#1061, #1077].

### Évolutions techniques
- Mise à jour vers Nuxt 4.4 [#1038].
- Mise à jour vers Nuxt 4.3 [#1037].
- Mise à jour de `geopf-extensions-openlayers` vers la version 1.0.0-beta.10 [#1085].
- Optimisation des dépendances [#1086].
- Alignement du README avec Nuxt 4 [#1068].
- Correction de side effects dans certaines mises à jour [#1079, #1080].
- Ignorer le répertoire du cache pnpm local [#1071].
- Utilisation d'images SVG optimisées avec svgo [#1057].
- Ajout d'une première implémentation de visualisation (POC) [#963].

### Autres changements
- Correction de l'affichage des images SVG statiques [#1057].
- Correction d'un bug lié à la visibilité des champs mobiles [#1058].
- Correction d'un problème d'affichage sur la nouvelle page /explore [#1056].
- Amélioration de l'affichage des callbacks en attente et ajout du sujet utilisateur [#1073].
