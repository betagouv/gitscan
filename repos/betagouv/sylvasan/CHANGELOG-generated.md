## Changelog : sylvasan (30 derniers jours, au 04/08/2026)

### Résumé
Ce mois a été marqué par l'introduction majeure de la fonctionnalité de "suivis" (follow-ups), permettant de réagir et d'ajouter des observations aux réponses existantes. L'expérience de terrain a été renforcée par des améliorations de la précision GPS et de la gestion des images, tandis que l'interface web a gagné en puissance grâce à de nouveaux outils de filtrage et de gestion des suivis.

### Évolutions fonctionnelles
- **Gestion des suivis (Follow-ups) :** 
    - Possibilité de créer des suivis directement via l'URL d'une réponse.
    - Ajout d'observations sur les réponses d'autres utilisateurs avec distinction visuelle des répondants (couleurs des pins et noms).
    - Interface web complète pour la création, la modification et la suppression des suivis.
- **Géolocalisation et Cartographie :**
    - Amélioration de la précision GPS et ajout d'un indicateur de précision avec échelle visuelle.
    - Affichage d'un cercle de précision sur la carte et mise à disposition du bouton de géolocalisation sur l'ensemble des cartes.
- **Gestion des enquêtes et réponses :**
    - Fonctionnalité de duplication d'enquêtes.
    - Amélioration de la recherche via des filtres (notamment par organisation) et une pagination des résultats.
    - Ajout de valeurs par défaut pour les champs de type sélection, radio et autocomplétion.
- **Interface Utilisateur (UI/UX) :**
    - Optimisation de la visibilité des champs obligatoires (styles, labels et espacements).
    - Amélioration de l'affichage des images (vue complète et composant dédié sur le web).
    - Mise à jour des libellés pour plus de clarté (boutons d'envoi et de sauvegarde en brouillon).
    - Correction de l'ordre des champs dans l'application mobile.

### Évolutions techniques
- **Architecture et Refactoring :**
    - Migration de la logique de validation (Zod) et de la sélection d'organisation vers des *composables* pour une meilleure réutilisation.
    - Optimisation du stockage des images dans les champs de type tableau : passage d'un stockage en base64 à un stockage par ID.
- **Backend et API :**
    - Implémentation des modèles, migrations et endpoints API nécessaires à la gestion des suivis.
    - Ajout du support PostGIS pour les champs de réponse géospatiaux.
- **Mobile :**
    - Mises à jour des versions pour les applications Android et iOS.
- **Qualité et Accessibilité :**
    - Amélioration de l'accessibilité via l'ajout d'attributs ARIA.
    - Renforcement de la couverture de tests (notamment sur les membres et les suivis).

### Autres changements
- **Documentation :** Ajout d'un document détaillant les permissions par rôle.
- **Maintenance :** Corrections TypeScript et nettoyage de code suite aux revues.
