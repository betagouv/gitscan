## Changelog : mon-entreprise (30 derniers jours, au 24 août 2026)

### Résumé
Ce mois a été marqué par une refonte profonde de l'architecture interne pour rendre la gestion des simulateurs plus robuste et évolutive. Parallèlement, l'expérience de développement a été grandement améliorée grâce à l'automatisation des environnements de test pour chaque modification. Côté utilisateur, la précision des calculs (notamment sur la RGDU et les retraites 2026) a été renforcée et l'interface a bénéficié de plusieurs améliorations visuelles.

### Évolutions fonctionnelles
- **Précision des calculs** :
  - Correction de la valeur du SMIC utilisée pour le calcul de la RGDU.
  - Mise à jour des taux de la retraite complémentaire (CARMF et CARCDSF) pour l'année 2026.
- **Interface et design** :
  - Ajout du header et du footer sur la page d'accueil (version Next.js).
  - Amélioration de l'aspect visuel avec de nouvelles images de prévisualisation pour les simulateurs et de nouvelles illustrations (ex: page demande-mobilité).
  - Corrections de coquilles dans les messages de contact du pied de page et ajustements de mise en page (centrage de boutons).

### Évolutions techniques
- **Refonte de l'architecture des simulateurs** :
  - Migration vers un système de routage explicite, remplaçant l'ancien système de dispatch par configuration.
  - Séparation stricte entre les métadonnées (données pures pour le SEO, le plan du site, etc.) et les configurations de pages (composants React, paramètres de simulation).
  - Nettoyage massif du code obsolète et des fichiers de configuration redondants.
- **Optimisation du workflow CI/CD** :
  - Mise en place de "Review Apps" sur Clever Cloud : chaque Pull Request génère désormais un environnement de test temporaire avec un lien direct dans le commentaire de la PR.
  - Amélioration de la gestion des déploiements et de la durée des jobs sur Clever Cloud.
- **Performances et outils** :
  - Optimisation du temps de chargement via le chargement à la demande (*lazy loading*) du bouton de suggestion de réponses.
  - Mise à jour de la chaîne de développement : TypeScript, Vite, Vitest et Prettier.
  - Amélioration de la gestion des assets et normalisation de l'importation des ressources entre les environnements Vite et Next.js.
  - Refactorisation des composants d'intégration (Iframe) pour une meilleure gestion des propriétés.

### Autres changements
- **Documentation** :
  - Précisions apportées sur l'utilisation du SMIC dans les calculs.
  - Documentation mise à jour concernant l'infrastructure Clever Cloud et la gestion des métadonnées des simulateurs.
  - Amélioration de la rédaction du README.
- **Maintenance** :
  - Nettoyage du dépôt (suppression d'images et de dossiers inutilisés).
  - Suppression de commentaires et de types de code obsolètes.
