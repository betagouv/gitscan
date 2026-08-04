## Changelog : drive (30 derniers jours, au 03/08/2026)

### Résumé
Cette période a été marquée par un effort majeur sur la gestion du stockage et des quotas, offrant aux utilisateurs une meilleure visibilité sur leur espace disponible et des messages d'erreur plus explicites. Les capacités de partage ont été enrichies, notamment par la possibilité de partager des fichiers en masse ou avec des contacts importés depuis un fichier. Enfin, l'interface a été affinée pour améliorer la communication via un nouveau widget de messages et une navigation plus fluide dans les filtres de recherche.

### Évolutions fonctionnelles
- **Gestion du stockage et des quotas** : 
    - Introduction d'une jauge de stockage visuelle et d'un modal de configuration.
    - Affichage de messages d'erreur spécifiques lors de l'échec d'une action due à un quota dépassé.
    - Possibilité d'exclure certains éléments du calcul du quota de stockage.
    - Ajout d'une commande pour accorder un stockage illimité (administration).
- **Partage et collaboration** : 
    - Ajout du partage groupé d'éléments (batch share).
    - Possibilité d'importer des contacts depuis un fichier lors du partage d'un élément.
    - Renforcement de la sécurité : les actions de duplication et de déplacement vers la racine sont désormais soumises aux droits d'upload.
- **Interface utilisateur (UI)** : 
    - Intégration d'un widget de messages accessible depuis la page d'accueil ou le menu d'aide.
    - Amélioration de l'ergonomie des filtres de recherche (défilement sur petits écrans, réinitialisation facilitée).
    - Mise à jour de l'interface de partage pour s'adapter aux nouveaux composants du design system (UI-Kit).
- **Administration** : 
    - Amélioration de l'interface de détection de malwares avec l'affichage de la taille des fichiers et de leur existence.

### Évolutions techniques
- **Architecture et API** : 
    - Refonte du système de droits (entitlements) pour intégrer la gestion des limites de stockage locales.
    - Optimisation des performances via une meilleure gestion de l'invalidation du cache de stockage lors des écritures.
    - Déplacement de la logique de synchronisation des accès des descendants vers un service dédié.
    - Modification de l'endpoint des éléments favoris vers `/items/favorites/`.
- **Infrastructure et Sécurité** : 
    - Durcissement de la configuration Docker et mise à jour de l'image Collabora.
    - Correction de vulnérabilités de sécurité (notamment sur la bibliothèque `joserfc`).
    - Rendre la liste d'accès (ACL) d'upload configurable via le backend.
- **Qualité logicielle** : 
    - Amélioration de la couverture des tests de bout en bout (E2E) sur les fonctionnalités de partage et de conversion de documents.
    - Mise à jour des configurations de tests unitaires (Jest).

### Autres changements
- Passage à la version **0.20.0**.
- Mise à jour du composant UI-Kit.
- Corrections orthographiques dans les messages système concernant les quotas.
- Mise à jour de la documentation du projet.
