## Changelog : docs (30 derniers jours, au 13/11/2026)

### Résumé
Cette période a été marquée par une amélioration significative de la collaboration et de la gestion documentaire. L'introduction des mentions d'utilisateurs et d'une meilleure gestion des sous-documents fluidifie le travail d'équipe. Parallèlement, des outils d'administration plus puissants ont été ajoutés pour faciliter la gestion des comptes et des contenus, tandis que la sécurité et la robustesse de l'infrastructure ont été renforcées.

### Évolutions fonctionnelles
- **Collaboration et mentions** :
    - Possibilité de mentionner des utilisateurs dans l'éditeur et les commentaires via un menu déroulant "@".
    - Ajout de notifications pour les utilisateurs mentionnés.
    - Amélioration de l'expérience de mention avec l'intégration du sélecteur d'emojis Frimousse.
- **Navigation et interface utilisateur** :
    - Navigation fluide (smooth scroll) vers les blocs liés au sein d'un même document.
    - Affichage d'un bloc dédié listant les sous-documents.
    - Refonte de la page d'erreur 500 et amélioration de l'interface du chargeur d'upload.
    - Amélioration de l'accessibilité (boutons de navigation, lecteurs d'écran).
- **Gestion documentaire** :
    - Amélioration de la gestion des sous-documents (affichage du compteur, droits de suppression restreints aux créateurs).
    - Optimisation de l'export PDF (gestion des liens internes et des polices).
    - Correction de l'affichage des titres longs et des éléments de recherche.
- **Administration** :
    - Nouveaux outils pour la gestion des utilisateurs : fusion de comptes, transfert de documents entre utilisateurs et visualisation de la dernière connexion.
    - Amélioration de la réconciliation des utilisateurs et de la gestion des doublons.

### Évolutions techniques
- **Backend et Performance** :
    - Optimisation de la recherche d'utilisateurs via l'utilisation d'index trigrammes.
    - Création d'un endpoint dédié pour la gestion des droits d'accès (abilities).
    - Amélioration de la surveillance des workers Celery via des fichiers heartbeat.
- **Sécurité et Infrastructure** :
    - Application de correctifs de sécurité critiques sur Next.js, Vite, Sentry et d'autres dépendances.
    - Sécurisation des images Docker (utilisation d'images distroless pour yhub et de bases Nginx non privilégiées).
    - Optimisation des scans de sécurité (Trivy) pour ne cibler que les branches de release.
- **Intelligence Artificielle** :
    - Ajout de nouvelles compétences (skills) pour les agents IA.
    - Amélioration de la résilience et de l'efficacité des agents.
- **Qualité et CI/CD** :
    - Stabilisation des tests frontend (correction des avertissements "act").
    - Amélioration des tests E2E.

### Autres changements
- **Documentation** : Mise à jour des guides de contribution (AGENTS.md, UPGRADE.md) et organisation des variables d'environnement.
- **Internationalisation** : Mise à jour des chaînes de traduction et intégration du contexte pour Crowdin.
