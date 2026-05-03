## Changelog : dictaphone (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur le développement d'une application mobile pour Dictaphone, en parallèle de l'amélioration de l'interface web et de la correction de bugs.  Une fonctionnalité clé est l'intégration de la transcription automatique des enregistrements vers des outils de documentation. Des améliorations significatives ont également été apportées à l'authentification et à la sécurité, notamment avec l'implémentation de JWT et PKCE pour l'application mobile.

### Évolutions fonctionnelles
- Ajout d'un lien "Supprimer le compte" sur l'écran d'informations de l'application mobile.
- Possibilité de réessayer les uploads ayant échoué sur l'interface web.
- Ajout d'un lien vers la documentation sur l'écran d'informations de l'application mobile.
- Implémentation d'une fonctionnalité de suppression par glissement (swipe to delete) dans l'application mobile.
- Ajout d'une fonctionnalité de copie du texte de la transcription dans le presse-papier sur l'interface web.
- Intégration de la possibilité d'ouvrir la transcription dans un outil de documentation externe.
- Ajout d'une fonctionnalité de téléchargement de l'application mobile depuis l'interface web.
- Mise en place d'une logique d'authentification plus sécurisée avec JWT et PKCE pour l'application mobile.
- Ajout d'un écran d'informations dans l'application mobile avec un lien vers la documentation.
- Ajout d'une fonctionnalité de déconnexion (logout) dans l'application mobile.
- Amélioration de la robustesse de l'enregistrement audio dans l'application mobile.

### Évolutions techniques
- Mise à jour des dépendances backend et des fichiers Docker.
- Généralisation des tests backend.
- Suppression temporaire des vérifications liées au changelog et au linting dans le CI.
- Correction d'un problème dans le fichier CI principal.
- Intégration du linting mobile dans le CI.
- Correction d'une indentation dans le fichier Helm pour le backend Celery.
- Ajout de la gestion des jetons JWT avec PKCE pour l'authentification mobile.
- Amélioration du logging en cas d'échec de la transcription.
- Mise en place d'un système de publication des images Docker sur les branches d'intégration.
- Ajout de la prise en charge du format audio `m4a` sur le backend.
- Amélioration de la gestion des erreurs et des logs.
- Refonte de la structure du code pour l'application mobile (React Native).
- Mise en place de Prettier et ESLint pour le code mobile.
- Configuration de l'orientation de l'écran sur Android pour l'application mobile.
- Utilisation de la bibliothèque `react-native-nitro-player` pour la lecture audio sur mobile.

### Autres changements
- Publication des versions 1.0.2 (mobile), 0.5.3 (web/backend), 1.0.1 (mobile), 0.5.2 (web/backend), 0.5.1 (web/backend) et 1.0.0 (mobile).
- Mise à jour des documents légaux sur l'interface web.
- Correction de problèmes de typographie et de formatage dans le code.
- Ajout de données de test pour faciliter la prise de captures d'écran.
- Traduction de certains éléments de l'interface utilisateur en français.
- Suppression de l'écriture inclusive dans le code.
- Mise à jour du logo et des icônes de l'application mobile.
- Amélioration de la gestion des erreurs et des logs.
- Suppression de code obsolète.
- Correction de bugs mineurs et améliorations de la performance.
