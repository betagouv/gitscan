## Changelog : abrege (30 derniers jours, au 07/10/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec l'intégration de fonctionnalités d'analyse sémantique avancées (questions-réponses, extraction d'entités et de sujets) désormais configurables à la demande. L'interface utilisateur a été modernisée pour offrir une meilleure navigation, tandis que la sécurité et la fiabilité du système ont été renforcées, tant pour les utilisateurs finaux que pour les développeurs utilisant le SDK.

### Évolutions fonctionnelles
- **Nouvelles capacités d'analyse** : Ajout de l'extraction de questions-réponses (Q&A), d'entités, de sujets et de segments de texte, avec la possibilité de les activer ou désactiver selon les besoins.
- **Amélioration de l'interface utilisateur** : 
    - Affichage de la liste des tâches sous forme de cartes (tiles) pour une meilleure lisibilité.
    - Ajout de fonctions de recherche dans les fenêtres de détails (modales) pour les entités, les segments et les questions-réponses.
    - Intégration d'un nouveau pied de page (AppFooter) incluant la gestion de la version de l'application.
- **Sécurité et Authentification** : 
    - Mise en place d'une authentification plus robuste via un modèle BFF (Backend-for-Frontend) utilisant des cookies de session sécurisés (httpOnly).
    - Ajout du support pour le renouvellement automatique des jetons d'accès (refresh tokens).
- **Évolutions du SDK Python** : 
    - Extension des capacités de récupération des données (Q&A, entités, relations, sujets, segments).
    - Support de l'authentification par identifiant et mot de passe.

### Évolutions techniques
- **Modernisation de la CI/CD** : 
    - Harmonisation complète des pipelines de déploiement avec le projet `ocr-api`.
    - Intégration directe du chart Helm dans le dépôt pour simplifier les déploiements.
- **Sécurisation de l'infrastructure** : Passage à une exécution en mode "non-root" pour l'ensemble des images Docker afin de renforcer la sécurité des conteneurs.
- **Optimisation du moteur OCR** : Amélioration de la gestion de l'authentification, de l'initialisation du client et de la robustesse face aux erreurs de connexion.
- **Refactoring et maintenance** : 
    - Nettoyage approfondi du code : suppression des données de test (mock), du code mort et des dépendances inutiles.
    - Optimisation de la gestion des tâches : les sous-tâches OCR ne sont désormais supprimées qu'une fois le document complet traité.
    - Amélioration de la structure globale du code pour une meilleure maintenabilité.

### Autres changements
- **Documentation** : Enrichissement de la documentation avec des captures d'écran pour les instructions d'analyse et mise à jour des guides d'utilisation du SDK.
- **Configuration** : Harmonisation des variables d'environnement (OpenAI, Redis) et nettoyage des fichiers `.gitignore`.
