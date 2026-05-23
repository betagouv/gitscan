## Changelog : meet (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur, notamment avec l'introduction d'une fonctionnalité "Picture-in-Picture" pour les documents partagés et des améliorations significatives de la réactivité et de l'accessibilité de l'interface. Des améliorations de la sécurité et de la configuration des salles ont également été apportées, ainsi que le début de l'intégration d'un add-in pour Microsoft Outlook.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité "Picture-in-Picture" (PiP) pour les documents partagés, incluant une barre de contrôle, un menu d'options et une indication de l'état de la connexion. [#1247]
- Amélioration de l'accessibilité de la barre d'outils de réactions, notamment pour les utilisateurs mobiles.
- Possibilité pour les administrateurs de configurer si tous les participants peuvent couper le son des autres.
- Amélioration de l'assignation des intervenants lors de la transcription audio.
- Ajout d'un lien direct vers l'ouverture des enregistrements dans les emails de notification.
- Clarification du texte du lien de téléchargement de la transcription audio en français.

### Évolutions techniques
- Refactorisation de composants frontend pour améliorer la clarté et la maintenabilité du code.
- Synchronisation des mises à jour de la configuration des salles entre le backend et le frontend.
- Mise en place d'un mécanisme de validation de la configuration des salles avec un schéma Pydantic.
- Amélioration de la gestion des erreurs et de la robustesse du processus d'enregistrement.
- Introduction d'un système d'authentification pour les add-ons.
- Utilisation de `uv` pour la gestion des dépendances dans l'environnement des agents.
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité et améliorer les performances.
- Amélioration de la gestion des jetons CSRF pour une meilleure conformité aux conventions Django.

### Autres changements
- Mise à jour de la documentation et du changelog.
- Ajout de tests unitaires pour le service de gestion des jetons JWT.
- Correction de bugs mineurs dans l'add-in Outlook (en phase alpha).
- Amélioration des logs pour faciliter le débogage de l'assignation des intervenants.
- Suppression de certaines dépendances obsolètes.
- Correction de problèmes de positionnement de l'interface utilisateur.
- Mise à jour des dépendances frontend et backend.
- Ajout d'une configuration Nginx pour le frontend DINUM.
- Amélioration de la gestion des polices d'accessibilité.
- Ajout d'une option pour configurer l'encodage des enregistrements LiveKit Egress.
- Correction de problèmes liés à la gestion des états de connexion.
