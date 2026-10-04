## Changelog : abrege (30 derniers jours, au 02/10/2026)

### Résumé
Cette période est marquée par le passage à la version 3.4.0, apportant des capacités d'analyse sémantique enrichies (questions-réponses, extraction d'entités et de sujets) désormais configurables. L'expérience utilisateur a été modernisée avec une nouvelle interface de gestion des tâches et une sécurité renforcée grâce à une nouvelle méthode d'authentification.

### Évolutions fonctionnelles
- **Nouvelles capacités d'analyse** : Ajout de l'extraction de questions-réponses (Q&A), d'entités, de relations, de sujets et de segments (chunks), désormais disponibles en option.
- **Amélioration de l'interface utilisateur** :
    - Affichage de la liste des tâches sous forme de tuiles (tiles) pour une meilleure lisibilité.
    - Ajout d'une fonction de recherche dans les fenêtres modales (segments, entités et Q&A).
    - Intégration d'un composant de pied de page (AppFooter) et gestion de la pagination des données.
- **Sécurité et Authentification** :
    - Mise en place de l'authentification BFF (Backend For Frontend) utilisant des cookies de session `httpOnly`.
    - Support du rafraîchissement automatique des jetons d'accès (refresh tokens).
- **Enrichissement du SDK** :
    - Nouvelles méthodes pour récupérer les données extraites (Q&A, entités, etc.).
    - Support de l'authentification par identifiant et mot de passe.

### Évolutions techniques
- **Architecture et Backend** :
    - Refonte des services de transcription audio et vidéo.
    - Optimisation de la gestion de l'OCR : amélioration de l'initialisation du client, de la gestion des erreurs et de l'authentification.
    - Suppression des données de test (mock data) et de la logique de contournement du SSO (SSO bypass) pour plus de sécurité.
- **DevOps et Infrastructure** :
    - Harmonisation des pipelines CI/CD avec le projet `ocr-api`.
    - Migration du chart Helm directement dans le dépôt du projet.
    - Sécurisation des conteneurs Docker en forçant l'exécution en mode non-root.
    - Optimisation du développement local via le remplacement de MinIO par RustFS.
- **Observabilité et Performance** :
    - Amélioration de la clarté des logs (réduction du bruit généré par les bibliothèques de modèles et configuration d'Uvicorn).
    - Optimisation de la suppression des sous-tâches OCR pour ne les traiter qu'une fois le document complet terminé.

### Autres changements
- **Documentation** : Ajout de captures d'écran pour les champs d'instructions d'analyse et documentation des routes de l'API.
- **Nettoyage** : Suppression de code mort et de configurations liées aux anciens connecteurs de documents.
- **Configuration** : Harmonisation des variables d'environnement (OpenAI, Redis) et mise à jour du `.gitignore` pour les répertoires de modèles.
