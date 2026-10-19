## Changelog : mycollections (30 derniers jours, au 17 octobre 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'expérience utilisateur, rendant l'interface plus intuitive, accessible sur mobile et plus claire grâce à des messages en français. De nouvelles fonctionnalités de pilotage de la qualité ont été introduites pour mieux contrôler les réponses de l'IA. Parallèlement, l'infrastructure technique a été modernisée pour garantir des déploiements plus robustes et une sécurité renforcée.

### Évolutions fonctionnelles
- **Génération et Qualité** : Introduction de la génération de questions par persona, d'un jeu de questions de référence et d'une nouvelle page dédiée au pilotage de la Qualité [#61].
- **Recherche et Catalogue** : 
    - Amélioration du catalogue avec des catégories repliables et une meilleure visibilité des titres.
    - Mise en place d'un nouveau contrat de recherche (MirAI) via de nouvelles API de recherche.
    - Ajout d'indicateurs de précision sur les résultats de recherche (seuils minimums).
- **Expérience Utilisateur (UX) et Accessibilité** :
    - Optimisation de l'ergonomie mobile (menu repositionné, gestion du focus clavier, navigation facilitée).
    - Généralisation des messages d'erreur et d'information en français pour une meilleure compréhension.
    - Amélioration de la consultation des sources (aperçus au survol, lecture d'extraits).
    - Interface de création et de publication simplifiée (étapes de création plus claires, historique de publication lisible).
- **Gestion des Collections** : 
    - Amélioration des fiches de collection (onglets, consultation du corpus, boutons d'action explicites).
    - Nouveau système de gestion des demandes et de satisfaction des utilisateurs.

### Évolutions techniques
- **Déploiement et CI/CD** : 
    - Intégration d'ArgoCD pour la gestion des déploiements.
    - Mise en place d'une nouvelle chaîne de CI/CD (v0.23.0) incluant les environnements de preview et de bêta.
    - Amélioration des charts Helm pour une meilleure gestion des versions de l'application.
- **Sécurité et Accès** :
    - Renforcement des contrôles d'accès sur l'ensemble des routes de l'API.
    - Gestion des droits "Superadmin" via des variables d'environnement.
    - Correction de vulnérabilités critiques via la mise à jour de l'image de base Nginx.
- **Fiabilité et Performance** :
    - Amélioration de la résilience de l'indexation (reprise automatique après un redémarrage).
    - Optimisation de la compatibilité avec OpenRAG pour la lecture des métadonnées des sources.
    - Unification de la configuration frontend via un fichier `/config.json` pour simplifier l'usage d'une image unique.
- **Outils et Tests** :
    - Migration de la gestion des dépendances vers `uv` pour plus de rapidité et de fiabilité.
    - Renforcement de la couverture de tests avec une nouvelle suite de tests de bout en bout (E2E) couvrant les parcours critiques.

### Autres changements
- **Documentation** : Mise à jour de la documentation technique (stratégie de branches, procédures de déploiement neutres) et du guide utilisateur (README).
- **Nettoyage** : Retrait des identifiants d'infrastructure sensibles du code source pour plus de sécurité.
