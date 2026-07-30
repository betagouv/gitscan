## Changelog : agora-front (30 derniers jours, au 28 juillet 2026)

### Résumé
Cette mise à jour améliore la stabilité et la sécurité de l'application, notamment au niveau des liens profonds (deeplinks) et de la gestion des certificats. Des corrections ont également été apportées à l'affichage de la page profil et à l'intégration du design.

### Évolutions fonctionnelles
- Correction d'un problème d'affichage de la page profil, qui pouvait apparaître vide. [#252](https://github.com/agora-gouv/agora-front/pulls/252)
- Correction de la redirection après le questionnaire sociodémographique. [#257](https://github.com/agora-gouv/agora-front/pulls/257)
- Amélioration du design, notamment des breadcrumbs et du bandeau de pied de page. [#255](https://github.com/agora-gouv/agora-front/pulls/255)

### Évolutions techniques
- Ajout de SHA256 pour le débogage des liens profonds (deeplinks). [#254](https://github.com/agora-gouv/agora-front/pulls/254)
- Correction des empreintes de certificats SHA256. [#253](https://github.com/agora-gouv/agora-front/pulls/253)
- Correction de la configuration des liens `assetlinks` et `apple-app-site-association` pour une meilleure compatibilité avec les plateformes mobiles. [#251](https://github.com/agora-gouv/agora-front/pulls/251)
- Ajout des fichiers nécessaires pour les liens profonds. [#250](https://github.com/agora-gouv/agora-front/pulls/250)
