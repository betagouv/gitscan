## Changelog : dictaphone (30 derniers jours, au 11 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment sur mobile, avec une gestion améliorée de l'enregistrement, du téléchargement et de la reprise d'enregistrements interrompus. Des fonctionnalités de régénération de transcriptions et de gestion des erreurs ont été ajoutées. L'accessibilité a également été améliorée sur le frontend, et la configuration de la politique de données est maintenant plus flexible.

### Évolutions fonctionnelles
- Possibilité de reprendre un enregistrement interrompu sur mobile.
- Affichage d'une alerte lorsque l'enregistrement web est lancé depuis un appareil mobile.
- Affichage de l'état de la transcription sous forme de badge sur le frontend.
- Affichage des informations relatives à la politique de données sur la page d'enregistrement.
- Ajout d'une option pour régénérer une transcription échouée, accessible depuis le menu des fichiers et via un swipe sur mobile.
- Possibilité de copier le texte de la transcription.
- Ajout d'actions supplémentaires (copier, ouvrir dans Indoc) au menu des fichiers.
- Amélioration de l'interface utilisateur de la liste des enregistrements.
- Ajout d'une indication visuelle du niveau sonore pendant l'enregistrement.
- Possibilité de télécharger un fichier non encore téléchargé.
- Gestion des liens profonds (deeplinks) pour la déconnexion sur mobile.
- Amélioration de la robustesse du composant d'enregistrement sur mobile.
- Affichage d'un message d'erreur plus clair en cas de problème de téléchargement.
- Ajout de sons de démarrage et d'arrêt de l'enregistrement sur mobile.
- Amélioration de l'accessibilité de l'application web (titres, labels ARIA, etc.).

### Évolutions techniques
- Mise à jour des dépendances du frontend.
- Amélioration de la gestion des erreurs et des timeouts.
- Refactorisation du code d'enregistrement sur le frontend.
- Ajout de tests pour la gestion des enregistrements hors ligne sur mobile.
- Mise à jour de Python et Django.
- Amélioration de la configuration de la politique de données (gestion automatique, exposition via un endpoint).
- Ajout de jobs cron pour la suppression des fichiers originaux et des fichiers supprimés.
- Amélioration de la sécurité avec l'utilisation de `secrets.compare_digest`.
- Ajout de logs plus détaillés pour faciliter le débogage des problèmes de connexion sur mobile.
- Support de plus de formats audio/vidéo.
- Amélioration de l'architecture du backend pour supporter la régénération des transcriptions.
- Mise à jour des librairies React Native Audio.

### Autres changements
- Mise à jour de la documentation (README, docs de développement).
- Correction de typos et amélioration de la lisibilité du code.
- Ajout d'un script pour automatiser les releases sur mobile.
- Ajout d'un lien vers la salle Matrix du projet dans le README.
- Amélioration des badges du README.
- Suppression de code inutile.
- Correction de problèmes de compatibilité iOS.
- Ajout de suivi PostHog pour les erreurs sur mobile.
- Configuration de l'agent utilisateur pour les requêtes.
