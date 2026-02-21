## Changelog : srdt (30 derniers jours)

### Résumé
Les dernières mises à jour de l'assistant virtuel SRDT se concentrent sur l'amélioration de la stabilité, la correction de bugs et l'ajout de nouvelles fonctionnalités pour une meilleure expérience utilisateur. Des améliorations ont été apportées à la gestion des conversations, à la sécurité des API et à la sauvegarde des discussions.

### Évolutions fonctionnelles
- Possibilité de sauvegarder l'historique des discussions en base de données (#298).
- Amélioration de l'interface web pour afficher des informations pendant le streaming de réponses (#306).
- Autorisation du département "dreets" (#301).
- Correction d'un bug empêchant l'annulation du streaming et la réponse lors d'une nouvelle conversation (#307).
- Correction de l'analyse et du filtrage des URLs dans les réponses de l'API (#293).

### Évolutions techniques
- Ajout de vérifications d'autorisation côté serveur pour les routes API non protégées (#302).
- Mise à jour des noms des modèles Albert.
- Ajout des secrets PostgreSQL aux variables d'environnement web (#300).
- Mise en place d'un cluster PostgreSQL (#299).

### Autres changements
- Correction d'une référence incorrecte dans l'API (#293, #309).
- Publication des versions 1.35.3, 1.35.2, 1.35.1, 1.35.0, 1.34.3, 1.34.2, 1.34.1 et 1.34.0.
