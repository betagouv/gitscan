## Changelog : mon-entreprise (30 derniers jours, au 17 novembre 2026)

### Résumé
Ce mois a été marqué par une transition technologique majeure vers Next.js, visant à améliorer les performances et le rendu des simulateurs. Parallèlement, plusieurs mises à jour réglementaires ont été effectuées, notamment sur les taux de cotisations 2026 pour les salariés et les calculs d'imposition pour les dividendes et les territoires d'outre-mer.

### Évolutions fonctionnelles
- **Simulateur Salarié** : Mise à jour des taux de cotisation des caisses CIBTP pour 2026 (incluant les taux de novembre 2026) et archivage des références antérieures.
- **Dividendes** : Correction du calcul de l'impôt et de la description de l'imposition au barème.
- **Lodeom** : Ajout de documentation et d'une modale explicative sur la régularisation ; correction du coefficient T pour Saint-Barthélemy et Saint-Martin.
- **Mayotte** : Correction du calcul de l'assiette sociale.
- **Expérience utilisateur** : Amélioration de l'affichage des nouveautés pour les visiteurs récurrents.

### Évolutions techniques
- **Migration Next.js** : Migration profonde de l'architecture vers Next.js, incluant le rendu côté serveur (SSR) pour les simulateurs et une gestion optimisée des métadonnées et des images.
- **Intégration des simulateurs** : Les simulateurs d'embauche et de salaire (brut/net) sont désormais servis sous Next.js, notamment via des intégrations en iframe.
- **Documentation** : Intégration de la documentation Publicodes directement via Next.js pour une meilleure cohérence.
- **Infrastructure & CI/CD** : 
    - Déploiement de "Review Apps" Next.js (incluant une version anglaise) pour les environnements de test.
    - Renforcement de la sécurité via le nettoyage de la politique de sécurité du contenu (CSP).
- **Architecture & Design System** : Refactorisation de l'adaptateur d'environnement et mise en conformité du design system avec les *Server Components*.

### Autres changements
- **Documentation** : Mise à jour du schéma d'architecture pour l'année 2026.
- **Nettoyage** : Suppression de clés de traduction orphelines et retrait de dépendances obsolètes (polyfill.io).
