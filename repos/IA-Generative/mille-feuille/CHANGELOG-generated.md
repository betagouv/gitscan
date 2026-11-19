## Changelog : mille-feuille (30 derniers jours, au 18 novembre 2026)

### Résumé
Ce mois-ci, mille-feuille a franchi une étape majeure dans l'autonomie de ses agents et la puissance de sa recherche. L'intégration de bases de connaissances externes, la capacité des agents à utiliser des outils (calculatrice, serveurs MCP) et une refonte architecturale centralisant l'intelligence dans le backend améliorent considérablement la réactivité de la plateforme. L'expérience utilisateur a également été enrichie par une interface plus accessible, un mode sombre et une meilleure visibilité sur la consommation des ressources.

### Évolutions fonctionnelles
- **Intelligence & Agents** : 
    - Les agents peuvent désormais utiliser des outils variés (calculatrice, gestion des dates, serveurs MCP) et être appelés directement dans le chat via des mentions (`@Nom`).
    - Amélioration de l'interaction : les agents peuvent désormais lire leurs analyses et interroger d'autres agents.
    - Introduction de questions suggérées et de réponses prêtes à l'emploi pour faciliter l'exploration des dossiers.
- **Recherche & Connaissances** : 
    - Mise en place d'une base de connaissances permettant d'ajouter des sources externes (via URL et authentification).
    - Nouvelle interface de recherche hybride permettant de naviguer entre les résultats lexicaux et sémantiques.
- **Analyse de documents** : 
    - L'extraction sémantique par LLM est désormais plus précise, incluant la localisation textuelle (spans et bounding boxes) des entités.
    - Possibilité de modifier ou de supprimer une analyse directement depuis sa page.
- **Interface & Administration** : 
    - Ajout d'un onglet "Modèles" pour l'administrateur afin de gérer les capacités et les modes des LLM.
    - Mise en place d'un suivi de la consommation de tokens pour les utilisateurs et les administrateurs.
    - Ajout du support du mode clair/sombre et amélioration globale de l'ergonomie (bulles d'info, composants de navigation).

### Évolutions techniques
- **Architecture** : 
    - Refonte majeure déplaçant l'exécution des agents, l'indexation de recherche et la logique de l'assistant du worker vers le backend pour une meilleure stabilité et performance.
    - Migration de l'indexation vers une approche "blue/green" pour permettre des reconstructions d'index sans interruption de service.
- **Infrastructure & Déploiement** : 
    - Optimisation du déploiement sur OpenShift (gestion des secrets TLS via Vault, profils légers et compatibilité SCC).
    - Intégration de Qdrant directement dans le chart Helm et possibilité de rendre KEDA optionnel.
    - Amélioration de la gestion des images via des registres paramétrables.
- **Traitement de données (OCR & Search)** : 
    - Migration de l'OCR vers `pp-ocrv6 tiny` au format ONNX pour plus d'efficacité.
    - Déploiement de pods spécialisés pour le layout, les tableaux et la vision via PaddleOCR.
    - Optimisation de la recherche hybride avec l'utilisation de vecteurs creux (BM25 français) et de l'indexation Qdrant.

### Autres changements
- **Accessibilité** : Mise en conformité de l'interface avec les standards DSFR et amélioration du support des lecteurs d'écran pour les alertes d'erreur.
- **Qualité & Documentation** : Mise à jour de la documentation Helm et des guides d'utilisation des outils d'agents ; amélioration de la stabilité des tests backend.
