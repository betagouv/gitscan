## Changelog : mon-entreprise (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives sur le simulateur pour les travailleurs frontaliers suisses, avec une refonte de l'expérience utilisateur et l'ajout de nouvelles fonctionnalités. Des corrections et des mises à jour ont également été apportées aux modèles de calcul, notamment pour Mayotte, ainsi qu'au comparateur de statuts. Des optimisations techniques ont été réalisées pour améliorer la configuration de l'environnement et la gestion des dépendances.

### Évolutions fonctionnelles
- **Simulateur frontalier suisse :** Ajout d'un nouveau simulateur pour le calcul de la cotisation maladie des travailleurs frontaliers en Suisse, avec une nouvelle interface utilisateur et la prise en compte de la fin d'affiliation, des revenus et de la situation de l'utilisateur.
- **Comparateur de statuts :**
    - Amélioration de l'affichage des réponses en vue liste.
    - Ajout de liens vers la documentation des objectifs de simulation.
    - Modification des libellés des questions concernant l'imposition.
    - Ajout de la carte du statut AE.
- **Modèles de calcul :**
    - Correction de l'application de la réforme de l'acre (critère = date de création de l'entreprise).
    - Correction de la participation de la CPAM en cas d'exonérations.
    - Correction de l'arrondi des cotisations RC et ID pour les conjoints collaborateurs PLR Cipav.
    - Mise à jour des taux de la retraite complémentaire CARMF et CARCDSF pour 2026.
    - Correction de l'application du plancher et du plafond de l'abattement sur l'assiette à Mayotte.
    - Suppression de la CSG-CRDS à Mayotte.
- **Documentation :** Mise à jour de la page de documentation sur la librairie de calcul et ajout de descriptions aux modèles.

### Évolutions techniques
- **Environnement :**
    - Refonte de la configuration de l'environnement avec un adaptateur portable pour Vite/Next.
    - Centralisation de la configuration de production via l'adaptateur.
    - Suppression du client Fabrique Social inutilisé.
- **API :**
    - Exposition des modèles TI et AS via l'API.
    - Refactorisation de la gestion des chemins du cache.
    - Réorganisation des middlewares de l'API.
- **Design System :**
    - Amélioration de la gestion des boutons et des champs de formulaire.
    - Correction de problèmes d'affichage sur Chrome et Edge.
- **Tests :** Correction des tests de l'API.

### Autres changements
- Mise à jour des paquets `modele-xx`.
- Correction de quelques clés de traductions manquantes.
- Amélioration de la documentation du simulateur TFS (masquage du menu et de la liste des outils).
- Correction de bugs mineurs et améliorations de la lisibilité du code.
- Ajout de documentation pour les nouvelles fonctionnalités.
