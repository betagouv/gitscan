## Changelog : drive (30 derniers jours, au 21 août 2026)

### Résumé
Ce mois-ci, le projet a principalement concentré ses efforts sur le renforcement de la sécurité de l'intégration WOPI et l'enrichissement des fonctionnalités de partage collaboratif. Les utilisateurs bénéficient désormais de méthodes de partage plus flexibles (partage groupé, import de contacts) et d'une meilleure accessibilité aux messages, tandis que la gestion des quotas de stockage devient plus granulaire.

### Évolutions fonctionnelles
- **Amélioration du partage :**
  - Possibilité de partager des éléments en masse via un nouvel endpoint dédié.
  - Ajout de la fonctionnalité d'importation de contacts depuis un fichier pour faciliter le partage d'un élément.
- **Interface utilisateur :**
  - Le widget de messages est désormais accessible directement depuis la page d'accueil et via le menu d'aide.
- **Gestion du stockage :**
  - Introduction d'un indicateur d'exclusion de quota sur les éléments, permettant de ne pas impacter le stockage utilisateur.
  - Ajout d'une commande permettant d'accorder un stockage illimité.
- **Corrections :**
  - Résolution d'un bug où les événements de glisser-déposer (drag events) s'échappaient de la fenêtre modale de partage.

### Évolutions techniques
- **Sécurité (WOPI) :**
  - Renforcement majeur de la sécurité des requêtes WOPI par la vérification systématique des signatures.
  - Mise en place d'un scan des fichiers écrits via WOPI et restriction des cibles de renommage pour éviter les manipulations non sécurisées.
  - Utilisation d'une liste d'autorisation (allowlist) statique pour la résolution des fichiers de template.
- **Architecture et Backend :**
  - Refactorisation de la synchronisation des accès des descendants vers un service dédié pour une meilleure maintenance.
  - Déplacement de l'endpoint API des éléments favoris vers `/items/favorites/`.
  - Correction de la documentation de l'endpoint API de la corbeille.
- **Infrastructure et CI/CD :**
  - Mise à jour des environnements de build et des jobs de génération d'emails vers Node 22.
  - Mise à jour de l'image Docker frontend vers Alpine 3.24.
- **Tests :**
  - Amélioration de la couverture de tests (E2E et Jest) pour le widget de messages et les flux de partage.

### Autres changements
- **Documentation :** Mise à jour du changelog pour inclure les détails sur les fonctionnalités d'exclusion de quota.
- **Maintenance :** Normalisation des fins de ligne du fichier `yarn.lock`.
