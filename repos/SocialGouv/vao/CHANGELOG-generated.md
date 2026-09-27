## Changelog : vao (30 derniers jours, au 23/09/2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes avec le déploiement de nouvelles fonctionnalités liées à la gestion des hébergements et à la création de sites. Parallèlement, des travaux majeurs de mise à jour technique (passage à Nuxt v4) et d'optimisation de l'infrastructure ont été réalisés pour améliorer la stabilité et la sécurité du système.

### Évolutions fonctionnelles
- **Hébergement** : Mise en place d'un nouveau parcours de création d'hébergement [#1535] et déploiement du module de migration [#1521, #1552].
- **Gestion des agréments** : Amélioration de la validation des agréments pour les DREETS [#1526, #1546], correction de l'affichage des titres [#1572] et résolution de plusieurs bugs liés à la mise à jour et au chargement des détails d'agrément [#1525, #1527, #1532].
- **Expérience utilisateur** : Création d'une nouvelle page de création de site pour Fusager [#1555], correction des liens contenus dans les emails [#1529] et exclusion des agréments supprimés des listes de récupération [#1530].
- **Corrections diverses** : Correction liée au rapatriement [#1566].

### Évolutions techniques
- **Migrations & Architecture** : Migration majeure vers Nuxt v4 [#1544], refonte de l'architecture des compétences IA [#1534] et séparation de la base de données documentaire [#1561].
- **Infrastructure & Sécurité** : Mise à jour vers Node 24 [#1549], optimisation de l'image Docker (passage à bookworm-slim) [#1562], suppression des utilisateurs PostgreSQL statiques pour renforcer la sécurité [#1573] et intégration de Talisman.
- **Qualité & Développement** : Mise en place de "feature flags" pour le module hébergement [#1533] et correction des sélecteurs de tests de bout en bout (E2E) suite à des changements d'interface [#1554].
