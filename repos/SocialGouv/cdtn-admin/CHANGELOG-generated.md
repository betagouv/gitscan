## Changelog : cdtn-admin (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette version apporte des améliorations au sitemap, notamment la gestion des URLs et le filtrage des types de documents. De nouvelles fonctionnalités d'analyse des contributions ont été ajoutées, permettant un suivi plus précis des vues mensuelles. Des corrections ont également été apportées concernant le parsing des documents et la gestion des alertes de suppression. Enfin, des améliorations techniques ont été réalisées pour le déploiement et la sauvegarde de la base de données.

### Évolutions fonctionnelles
- Le sitemap a été mis à jour pour inclure le slug de la convention collective dans l'URL [#1701](https://github.com/SocialGouv/cdtn-admin/issues/1701).
- Une nouvelle fonctionnalité permet de suivre les contributions par vues mensuelles [#1697](https://github.com/SocialGouv/cdtn-admin/issues/1697).
- Ajout du type "bon à savoir" pour les contributions [#1691](https://github.com/SocialGouv/cdtn-admin/issues/1691).
- Amélioration de l'analyse des contributions suite à des changements SEO [#1698](https://github.com/SocialGouv/cdtn-admin/issues/1698).
- Les alertes de suppression n'incluent plus les accords et statuts [#1696](https://github.com/SocialGouv/cdtn-admin/issues/1696).
- Prise en compte de la nouvelle URL pour la contribution "congés pour évènements familiaux" [#1699](https://github.com/SocialGouv/cdtn-admin/issues/1699).
- Ingestion des accords d'entreprise [#1702](https://github.com/SocialGouv/cdtn-admin/issues/1702).

### Évolutions techniques
- Mise à jour de la version de Node dans le CI.
- Migration des builds d'images de buildkit-service vers buildkit-operator [#1695](https://github.com/SocialGouv/cdtn-admin/issues/1695).
- Implémentation d'un script pour effectuer des dumps de la base de données à une date précise (PITR) [#1687](https://github.com/SocialGouv/cdtn-admin/issues/1687).
- Détection automatique des salaires en pourcentage du SMIC dans le challenger [#1689](https://github.com/SocialGouv/cdtn-admin/issues/1689).

### Autres changements
- Le fichier `next-env.d.ts` généré par Next.js est maintenant ignoré par le système de contrôle de version.
- Correction du parsing du document des IDCCs [#1694](https://github.com/SocialGouv/cdtn-admin/issues/1694).
- Mise en place d'un package Python pour l'analyse des statistiques [#1690](https://github.com/SocialGouv/cdtn-admin/issues/1690).
