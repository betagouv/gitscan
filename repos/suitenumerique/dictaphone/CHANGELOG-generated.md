## Changelog : dictaphone (30 derniers jours, au 25 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'application, notamment l'intégration de l'application mobile (iOS et Android) avec une authentification sécurisée, l'ajout de fonctionnalités de suppression et de restauration de fichiers, ainsi que l'intégration avec un service d'IA pour la transcription et la synthèse audio. L'interface utilisateur a également été améliorée, avec une attention particulière à la réactivité et à l'expérience mobile.

### Évolutions fonctionnelles
- Ajout d'une application mobile (iOS et Android) avec authentification via JWT et PKCE.
- Intégration de la suppression et de la restauration des enregistrements avec une page "Corbeille".
- Intégration avec un service d'IA externe pour la transcription et la synthèse des enregistrements.
- Possibilité d'ouvrir les transcriptions dans une application externe via un bouton "Ouvrir dans Docs".
- Ajout d'une page d'aide avec des liens de téléchargement des applications mobiles.
- Amélioration de l'interface utilisateur pour une meilleure réactivité et une expérience utilisateur optimisée sur mobile.
- Affichage de l'état de progression lors du téléchargement des fichiers.
- Ajout d'indicateurs visuels pour les enregistrements en cours de traitement.
- Amélioration de la gestion des erreurs et des messages d'information.
- Ajout d'une option pour afficher la durée des enregistrements.
- Possibilité de copier la transcription dans le presse-papier.

### Évolutions techniques
- Mise en place d'un système d'authentification JWT avec PKCE pour l'application mobile.
- Refonte de l'architecture backend pour supporter l'intégration avec le service d'IA externe.
- Amélioration de la gestion des logs pour faciliter le débogage.
- Mise à jour des dépendances pour bénéficier des dernières corrections et améliorations.
- Configuration du pipeline CI/CD pour déployer les images Docker sur les branches d'intégration.
- Ajout de tests unitaires pour valider le bon fonctionnement des nouvelles fonctionnalités.
- Amélioration de la gestion des fichiers audio (support de m4a).
- Mise en place d'un système d'analyse (PostHog) pour suivre l'utilisation de l'application.
- Amélioration de la gestion des erreurs lors de l'appel au service d'IA.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités.
- Amélioration de la structure du code pour une meilleure lisibilité et maintenabilité.
- Correction de typos et amélioration de la qualité du code.
- Ajout de commentaires pour expliquer le fonctionnement de certaines parties du code.
- Mise à jour des assets et des logos de l'application.
- Amélioration de la configuration du projet pour faciliter le développement et le déploiement.
- Suppression du code obsolète.
- Ajout de variables d'environnement pour configurer le comportement de l'application.
- Correction de problèmes de compatibilité avec certains navigateurs.
