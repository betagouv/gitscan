## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 12 août 2026)

### Résumé
Cette période a été marquée par une amélioration significative de la précision du traitement des documents (OCR et PDF) et une optimisation de l'expérience utilisateur pour la gestion des collections. L'interface est désormais plus intuitive et informative, tandis que la sécurité des processus d'intégration continue a été renforcée.

### Évolutions fonctionnelles
- **Nouvelle fonctionnalité d'importation** : Possibilité d'ajouter des documents HTML directement via une URL.
- **Amélioration de la gestion des collections** : 
    - Remplacement de la saisie manuelle des identifiants par un composant de sélection (menu déroulant) pour éviter les erreurs.
    - Affichage de l'identifiant des collections dans les listes pour faciliter la distinction entre des collections portant le même nom.
- **Amélioration de l'expérience utilisateur (UX)** : 
    - Remontée directe des erreurs d'indexation et de création de collection dans l'interface utilisateur.
- **Corrections de bugs** :
    - Correction de l'affichage de la liste des documents pour qu'elle respecte la collection sélectionnée.
    - Correction du processus de suppression pour garantir la cohérence entre les collections indexées et les documents miroirs.

### Évolutions techniques
- **Refonte du pipeline de traitement PDF/OCR** : 
    - Implémentation d'un convertisseur OCR JSON pour une meilleure extraction de la structure des documents (gestion améliorée des tableaux, des listes, des titres et de la table des matières).
    - Amélioration de l'assemblage des blocs de texte pour assurer la continuité entre les pages.
- **Optimisation du moteur de recherche (RAG)** : 
    - Ajout de métadonnées de positionnement (coordonnées des blocs dans la page) pour permettre un meilleur ordonnancement des paragraphes lors de la phase de récupération d'informations.
    - Détection des blocs de texte chevauchant deux pages pour améliorer la segmentation des données.
- **Évolutions de l'API** : Mise à disposition de nouveaux points de terminaison (endpoints) pour récupérer dynamiquement la liste des collections disponibles.
- **Sécurité et CI/CD** :
    - Renforcement de la sécurité de la chaîne de déploiement (désactivation des identifiants `git` dans les dépôts clonés).
    - Intégration de `zizmor` pour la validation de la configuration.
    - Mise à jour de sécurité de la bibliothèque `Docling`.
