## Changelog : st-home (30 derniers jours, au 20 avril 2026)

### Résumé
Les dernières mises à jour de st-home se concentrent sur l'amélioration de la carte de déploiement avec une version 2 enrichie de nouvelles données, le remplacement de Nginx par Caddy pour la gestion du reverse proxy, et des corrections de bugs concernant l'export CSV des statistiques et l'affichage de l'OPSN. Des améliorations de contenu et l'ajout de nouvelles pages "Commune" ont également été apportées.

### Évolutions fonctionnelles
- **Carte de déploiement améliorée :** Nouvelle version (v2) de la carte de déploiement avec affichage des services et des EPCI. [#56](https://github.com/suitenumerique/st-home/issues/56)
- **Nouvelles pages "Commune" :** Ajout de nouvelles pages dédiées aux communes. [#57](https://github.com/suitenumerique/st-home/issues/57)
- **Améliorations de contenu :** Mise à jour des textes sur les pages RPNT et OPSN. [#1625e83](https://github.com/suitenumerique/st-home/commit/1625e83)
- **Correction d'un lien brisé :** Correction du lien vers le webinaire. [#ce55982](https://github.com/suitenumerique/st-home/commit/ce55982)
- **Correction de l'ordre des services :** Correction de l'ordre d'affichage des services Proconnect. [#ce55982](https://github.com/suitenumerique/st-home/commit/ce55982)
- **Correction de l'export CSV :** Correction de l'export CSV pour les niveaux groupés dans les statistiques. [#79d0dc4](https://github.com/suitenumerique/st-home/commit/79d0dc4)

### Évolutions techniques
- **Remplacement de Nginx par Caddy :** Nginx a été remplacé par Caddy comme reverse proxy pour améliorer la performance et la configuration. [#58](https://github.com/suitenumerique/st-home/issues/58)
- **Utilisation des données du DeployCenter :** La carte de déploiement utilise désormais les données du DeployCenter pour afficher les partenaires. [#97ad622](https://github.com/suitenumerique/st-home/commit/97ad622)

### Autres changements
- **Correction de l'affichage de l'OPSN :** Suppression de l'affichage de l'OPSN avant l'étape d'intention. [#0bb0cb3](https://github.com/suitenumerique/st-home/commit/0bb0cb3)
