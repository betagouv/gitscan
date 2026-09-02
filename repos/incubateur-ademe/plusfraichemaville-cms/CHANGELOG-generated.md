## Changelog : plusfraichemaville-cms (30 derniers jours, au 01/09/2026)

### Résumé
Ce mois a été marqué par une mise à jour majeure de l'infrastructure technique du CMS, avec la migration vers Strapi 5 pour garantir la pérennité et la performance de l'outil. Côté contenu, les fiches solutions ont été simplifiées par le retrait des informations relatives aux aides régionales.

### Évolutions fonctionnelles
- Simplification des fiches solutions par la suppression des sections concernant les aides régionales.

### Évolutions techniques
- **Migration majeure** : Passage à Strapi 5 ([#30](https://github.com/incubateur-ademe/plusfraichemaville-cms/pull/30)) pour assurer la compatibilité avec les dernières versions du framework.
- **Gestion des paquets** : Migration de l'outil de gestion des dépendances de `npm` vers `pnpm` pour des installations plus rapides et efficaces.
- **Édition de contenu** : Passage à la version "Community Edition" du plugin CKEditor.
- **Base de données & Stockage** : 
    - Amélioration de la gestion du schéma de la base de données.
    - Correction d'un avertissement de dépréciation concernant les identifiants du fournisseur AWS S3.
- **Nettoyage et compatibilité** : Suppression du plugin de versionnement de contenu, devenu incompatible avec la nouvelle version de Strapi.

### Autres changements
- Mise à jour de la documentation (README) pour intégrer les nouvelles instructions d'utilisation avec `pnpm`.
