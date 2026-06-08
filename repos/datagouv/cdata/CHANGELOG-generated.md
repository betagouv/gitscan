## Changelog : cdata (30 derniers jours, au 5 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées à cdata au cours du dernier mois. Les principales évolutions concernent l'expérience utilisateur avec l'ajout de nouvelles fonctionnalités de recherche, d'affichage des contacts, et d'amélioration de l'explorateur tabulaire. Des corrections de bugs et des optimisations techniques ont également été réalisées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Recherche :** Ajout d'icônes personnalisables pour les types de recherche [#1109](https://github.com/datagouv/cdata/issues/1109).
- **Notifications :** Possibilité de marquer les notifications comme lues [#1103](https://github.com/datagouv/cdata/issues/1103) et ajout de nouvelles notifications [#1076](https://github.com/datagouv/cdata/issues/1076).
- **Explorateur tabulaire :** Améliorations apportées à l'explorateur tabulaire [#1070](https://github.com/datagouv/cdata/issues/1070).
- **Pages thématiques :** Ajout d'une page thématique [#1110](https://github.com/datagouv/cdata/issues/1110).
- **Affichage des contacts :** Amélioration de l'affichage des contacts [#1075](https://github.com/datagouv/cdata/issues/1075).
- **Réutilisation :** Réintroduction du lien entre les réutilisations et les sujets [#1082](https://github.com/datagouv/cdata/issues/1082) et correction de l'utilisation des champs "x-fields" dans l'onglet des réutilisations [#1102](https://github.com/datagouv/cdata/issues/1102).
- **Élections :** Ajout des données sénatoriales aux élections [#1091](https://github.com/datagouv/cdata/issues/1091).
- **Titre des cartes :** Possibilité de définir le titre des cartes [#1092](https://github.com/datagouv/cdata/issues/1092).
- **Accessibilité :** Amélioration de l'accessibilité de la recherche avec l'annonce du nombre de résultats et la possibilité de focus automatique [#1096](https://github.com/datagouv/cdata/issues/1096).

### Évolutions techniques
- **Dockerfile :** Utilisation de `NODE_ENV production` dans le Dockerfile pour optimiser la production [#1104](https://github.com/datagouv/cdata/issues/1104).
- **CORS :** Correction d'un problème de CORS dans les visualisations [#1116](https://github.com/datagouv/cdata/issues/1116) et gestion des identifiants lors de la nouvelle politique CORS [#1098](https://github.com/datagouv/cdata/issues/1098).
- **Optimisation des dépendances :** Ajout de dépendances optimisées [#1086](https://github.com/datagouv/cdata/issues/1086).
- **Composants :** Mise à jour des composants vers la version 1.1.2 [#1101](https://github.com/datagouv/cdata/issues/1101).
- **geopf-extensions-openlayers :** Mise à jour de `geopf-extensions-openlayers` vers la version 1.0.0-beta.10 [#1085](https://github.com/datagouv/cdata/issues/1085).

### Autres changements
- **Authentification 2FA :** Utilisation de l'URI QR code renvoyé par le backend pour l'authentification à deux facteurs [#1090](https://github.com/datagouv/cdata/issues/1090).
- **Logging :** Ajout d'un timestamp dans les logs [#1084](https://github.com/datagouv/cdata/issues/1084).
- **Admin :** Correction d'un bug dans la recherche de l'admin où la requête "q" ne réinitialisait pas la page [#1089](https://github.com/datagouv/cdata/issues/1089).
- **Rotation de mot de passe :** Ajout de la possibilité de faire tourner le mot de passe dans l'admin [#1078](https://github.com/datagouv/cdata/issues/1078).
- **Guides :** Correction des URLs des guides [#1077](https://github.com/datagouv/cdata/issues/1077).
- **Correction :** Correction pour masquer le bouton de rotation lorsque celui-ci a déjà été demandé [#1081](https://github.com/datagouv/cdata/issues/1081).
- **Correction :** Correction pour afficher l'ID de la ressource impactée dans les activités [#1123](https://github.com/datagouv/cdata/issues/1123).
- **Correction :** Correction pour masquer les statistiques de téléchargement sans jeux de données [#1113](https://github.com/datagouv/cdata/issues/1113).
- **Correction :** Correction d'un flash de recherche vide après la réinitialisation de la recherche [#1083](https://github.com/datagouv/cdata/issues/1083).
