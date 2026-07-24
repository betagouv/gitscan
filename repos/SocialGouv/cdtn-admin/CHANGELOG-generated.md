## Changelog : cdtn-admin (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, l'administration du site du Code du Travail Numérique a bénéficié d'améliorations concernant le sitemap, l'ingestion de données (accords d'entreprise), l'analyse des contributions et la gestion des alertes de suppression. Des corrections ont également été apportées pour assurer la bonne prise en compte des URLs et des données.

### Évolutions fonctionnelles
- Ajout d'une table pour le calcul du NPS (Net Promoter Score) permettant de mesurer la satisfaction des utilisateurs. [#1705](https://github.com/SocialGouv/cdtn-admin/issues/1705)
- Intégration de l'ingestion des accords d'entreprise. [#1702](https://github.com/SocialGouv/cdtn-admin/issues/1702)
- Ajout du suivi des contributions par nombre de vues mensuelles, offrant une meilleure analyse de l'utilisation du site. [#1697](https://github.com/SocialGouv/cdtn-admin/issues/1697)
- Mise à jour de l'analyse des contributions suite aux changements SEO récents. [#1698](https://github.com/SocialGouv/cdtn-admin/issues/1698)
- Correction des URLs sur la contribution congés pour les événements familiaux, améliorant la navigation et le référencement.
- Ajout du slug de la convention collective dans l'URL pour une meilleure identification des contenus. [#1701](https://github.com/SocialGouv/cdtn-admin/issues/1701)
- Correction du parsing des documents IDCCS. [#1694](https://github.com/SocialGouv/cdtn-admin/issues/1694)
- Les accords et statuts sont désormais exclus des alertes de suppression. [#1696](https://github.com/SocialGouv/cdtn-admin/issues/1696)

### Évolutions techniques
- Mise à jour de la version de Node.
- Migration des builds d'images de buildkit-service vers buildkit-operator, optimisant le processus de construction des images Docker. [#1695](https://github.com/SocialGouv/cdtn-admin/issues/1695)
- Mise en place d'un package Python pour l'analyse des statistiques. [#1690](https://github.com/SocialGouv/cdtn-admin/issues/1690)

### Autres changements
- Correction du filtrage du sitemap pour ne prendre en compte que les documents de type contribution.
- Amélioration de la gestion des URLs pour la contribution congés pour les événements familiaux.
