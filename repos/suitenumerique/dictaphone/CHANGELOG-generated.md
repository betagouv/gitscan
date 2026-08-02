## Changelog : dictaphone (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette version apporte des améliorations à l'expérience utilisateur, notamment lors du chargement de fichiers et de la visualisation des métadonnées de transcription. Des corrections de bugs ont été implémentées pour améliorer la robustesse de l'application, en particulier concernant la gestion des fichiers audio corrompus et des erreurs lors de la transcription. Plusieurs versions intermédiaires ont été publiées pour assurer une livraison continue des correctifs et améliorations.

### Évolutions fonctionnelles
- Amélioration de l'interface utilisateur : un indicateur de chargement est maintenant affiché pendant la vérification des fichiers.
- Support des fichiers MKV dans Chrome.
- En-tête des métadonnées de la transcription fixé pour une meilleure lisibilité.
- L'erreur "no_audio" est maintenant considérée comme un succès pour le backend, permettant une meilleure gestion des fichiers sans audio.
- L'URL de prévisualisation est masquée dans l'interface d'administration pour plus de sécurité.
- Amélioration du message d'erreur affiché lors du chargement d'un fichier audio corrompu.
- L'adresse email de l'utilisateur est incluse dans la requête de résumé.

### Évolutions techniques
- Configuration de la ré-exécution automatique des tâches Celery en cas d'échec.
- Amélioration de la gestion des erreurs dans le callback webhook : le motif de l'erreur est maintenant enregistré.
- Correction d'un problème de fin de chargement incorrect dans l'interface utilisateur.
- Augmentation de la taille maximale des fichiers autorisés en développement local.
- Correction d'un problème de timeout dans l'endpoint de retry.
- Correction d'un warning lié au fuseau horaire dans les tests.

### Autres changements
- Publication des versions v0.11.4, v0.11.3 et v0.11.2.
