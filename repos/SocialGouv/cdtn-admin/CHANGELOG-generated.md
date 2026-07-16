## Changelog : cdtn-admin (30 derniers jours, au 15 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'ingestion et de l'analyse des données, notamment concernant les accords d'entreprise et les contributions. Des corrections ont été apportées au sitemap et à la gestion des alertes de suppression. L'infrastructure de build a également été modernisée.

### Évolutions fonctionnelles
- Ajout de l'ingestion des accords d'entreprise. ([#1702](https://github.com/SocialGouv/cdtn-admin/issues/1702))
- Ajout du type "bon à savoir" pour les contributions. ([#1691](https://github.com/SocialGouv/cdtn-admin/issues/1691))
- Amélioration du suivi des contributions avec l'ajout du nombre de vues mensuelles. ([#1697](https://github.com/SocialGouv/cdtn-admin/issues/1697))
- Correction de l'URL pour la contribution "congés pour évènements familiaux" dans le sitemap. ([#1699](https://github.com/SocialGouv/cdtn-admin/issues/1699))
- Correction du parsing des documents IDCC pour une meilleure gestion des données. ([#1694](https://github.com/SocialGouv/cdtn-admin/issues/1694))
- Les accords et statuts ne sont plus inclus dans les alertes de suppression. ([#1696](https://github.com/SocialGouv/cdtn-admin/issues/1696))
- Possibilité de détecter automatiquement les salaires exprimés en pourcentage du SMIC dans le challenger. ([#1689](https://github.com/SocialGouv/cdtn-admin/issues/1689))

### Évolutions techniques
- Mise à jour de la version de Node.
- Modernisation de l'infrastructure de build en migrant les builds d'images de buildkit-service vers buildkit-operator. ([#1695](https://github.com/SocialGouv/cdtn-admin/issues/1695))
- Ajout d'un script pour effectuer un dump de la base de données à une date précise (PITR). ([#1687](https://github.com/SocialGouv/cdtn-admin/issues/1687))
- Ignorer le fichier `next-env.d.ts` généré par Next.js.

### Autres changements
- Mise à jour de l'analyse des contributions suite à des changements SEO. ([#1698](https://github.com/SocialGouv/cdtn-admin/issues/1698))
- Mise en place du package Python pour l'analyse des statistiques. ([#1690](https://github.com/SocialGouv/cdtn-admin/issues/1690))
