## Changelog : dictaphone (30 derniers jours, au 26 mai 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'application mobile, avec notamment la gestion de l'enregistrement hors ligne, la possibilité de relancer la transcription en cas d'échec, et une meilleure gestion des autorisations. L'application web a également bénéficié d'améliorations, notamment l'ajout de formats d'exportation avancés (SRT) et la possibilité de copier le texte des transcriptions. Des corrections de sécurité et des optimisations de performance ont été apportées à l'ensemble du projet.

### Évolutions fonctionnelles
- Ajout de la possibilité de relancer la transcription d'un fichier en cas d'échec via l'interface web et l'API. [#issue-lien-si-disponible]
- Implémentation de l'export de transcriptions au format SRT. [#issue-lien-si-disponible]
- Ajout des actions "Copier le texte" et "Ouvrir dans Indocs" au menu contextuel des fichiers. [#issue-lien-si-disponible]
- Amélioration de l'expérience utilisateur mobile avec la gestion de l'enregistrement hors ligne et la reprise automatique en cas de perte de connexion.
- Ajout d'un indicateur visuel du niveau sonore pendant l'enregistrement sur mobile.
- Possibilité de contourner l'écran de connexion sur mobile.
- Ajout d'un lien vers la salle Matrix dans le README.
- Amélioration de l'accessibilité de l'application web.
- Ajout d'une info-bulle sur le bouton d'upload.
- Mise à jour du menu d'aide.
- Ajout d'un son de démarrage/arrêt de l'enregistrement.
- Ajout d'une option pour n'autoriser l'upload qu'en WiFi sur mobile.
- Ajout d'un lien vers les mentions légales sur mobile.
- Amélioration de l'interface de suppression de compte sur mobile.

### Évolutions techniques
- Amélioration de la sécurité avec l'utilisation de `secrets.compare_digest` pour la comparaison de chaînes sensibles.
- Partage de l'adresse email de l'utilisateur avec le service de résumé.
- Mise à jour des dépendances pour renforcer la sécurité.
- Refactorisation du code pour améliorer la robustesse et la maintenabilité.
- Optimisation des performances de l'application web et mobile.
- Amélioration de la gestion des erreurs et des logs.
- Mise en place d'un script d'automatisation des releases mobiles.
- Ajout de tests unitaires et d'intégration.
- Amélioration de la configuration du pipeline CI/CD.
- Ajout d'un mécanisme pour nettoyer les fichiers temporaires et supprimés.
- Correction de problèmes liés à la gestion des états de l'enregistreur.
- Amélioration de la gestion des permissions sur mobile.
- Mise à jour des valeurs par défaut pour autoriser plus de types de fichiers.

### Autres changements
- Mise à jour de la documentation.
- Correction de fautes de frappe et amélioration de la lisibilité du code.
- Mise à jour des badges du README.
- Ajout de commentaires pour clarifier le code.
- Amélioration de la configuration Helm.
- Mise à jour des documents légaux.
- Ajout de données mock pour faciliter la prise de captures d'écran.
- Correction de problèmes de typographie dans l'application mobile.
- Ajout de métriques de suivi des erreurs sur mobile avec PostHog.
