## Changelog : cdtn-admin (30 derniers jours, au 3 juillet 2026)

### Résumé
Ce mois-ci, l'administration de cdtn-admin a bénéficié d'améliorations concernant la gestion des alertes de suppression des données, la correction de bugs liés au parsing de documents, l'ajout de nouvelles fonctionnalités pour l'analyse des données et la gestion des contributions, ainsi que des outils pour la sauvegarde et la restauration de la base de données. Des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un nouveau type de contribution "bon à savoir" [#1691](https://github.com/SocialGouv/cdtn-admin/issues/1691).
- Renommage de l'outil "Trouver sa CC" pour plus de clarté [#1669](https://github.com/SocialGouv/cdtn-admin/issues/1669).
- Les alertes de suppression des accords et statuts ne sont plus déclenchées par erreur [#1696](https://github.com/SocialGouv/cdtn-admin/issues/1696).
- Détection automatique des salaires exprimés en pourcentage du SMIC dans le challenger [#1689](https://github.com/SocialGouv/cdtn-admin/issues/1689).

### Évolutions techniques
- Mise en place d'un package Python pour l'analyse des statistiques, permettant une meilleure exploitation des données [#1690](https://github.com/SocialGouv/cdtn-admin/issues/1690).
- Ajout d'un script permettant de réaliser un dump de la base de données à une date précise, facilitant la restauration en cas de besoin (PITR) [#1687](https://github.com/SocialGouv/cdtn-admin/issues/1687).
- Correction du parsing des documents IDCC [#1694](https://github.com/SocialGouv/cdtn-admin/issues/1694).
- Le fichier `next-env.d.ts` généré par Next.js est maintenant ignoré par le système de contrôle de version.

### Autres changements
- Aucune information supplémentaire.
