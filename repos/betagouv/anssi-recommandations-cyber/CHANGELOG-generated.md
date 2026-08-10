## Changelog : anssi-recommandations-cyber (30 derniers jours, au 28 juillet 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la précision et de la fiabilité des réponses fournies par l'intelligence artificielle, notamment grâce à un meilleur système de citation des sources. L'interface utilisateur a également été enrichie pour offrir une meilleure lisibilité des documents (titres, dates) et de nouvelles fonctionnalités pratiques (bouton de copie), tout en assurant la compatibilité technique avec les dernières mises à jour de l'API Albert.

### Évolutions fonctionnelles
- **Amélioration de la qualité de l'IA** :
    - Renforcement des citations et des références aux recommandations de l'ANSSI dans les réponses.
    - Ajout d'un système de reclassement par LLM pour trier les sources de manière plus pertinente.
    - Stabilisation des réponses en fixant la température de l'IA à 0.
    - Optimisation des questions reformulées pour plus de cohérence.
- **Interface utilisateur et expérience (UI/UX)** :
    - Affichage des titres des documents et de leurs dates de mise à jour (remplaçant les noms de fichiers bruts).
    - Ajout d'un bouton pour copier rapidement les sources d'une réponse.
    - Intégration des icônes DSFR sur les boutons du carrousel.
    - Amélioration de la mise en page (aération des réponses détaillées) et mise à jour des messages d'accueil.
- **Contenu** :
    - Ajout d'un wording spécifique pour les tests internes de l'ANSSI.

### Évolutions techniques
- **Compatibilité API Albert 0.5.0** :
    - Migration des notebooks d'indexation et d'exploration pour supporter les nouveaux paramètres (`collection_id` au lieu de `collection`, `query` au lieu de `prompt`).
    - Mise à jour des routes de recherche et de récupération des segments de documents (`/search` et `/chunks`).
- **Architecture et Refactoring** :
    - Extraction de la logique de traitement des réponses pour séparer les données de l'API du métier.
    - Injection du module de reclassement directement dans le service Albert.
- **Sécurité et CI/CD** :
    - Intégration de `zizmor` pour la validation de la configuration.
    - Sécurisation des pipelines CI en désactivant les identifiants Git lors du clonage des dépôts.
- **Corrections de bugs** :
    - Résolution de problèmes de redirection FastAPI sur la ressource `/source`.
    - Correction de la génération d'URL pour l'accès aux documents (gestion des slashs).
    - Harmonisation du nombre de résultats retournés lors des recherches.

### Autres changements
- **Nettoyage et maintenance** :
    - Suppression de champs obsolètes, de feature flags et de contextes inutiles.
    - Refactorisation du code et réorganisation des tests pour plus de clarté.
