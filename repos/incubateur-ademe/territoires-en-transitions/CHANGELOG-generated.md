## Changelog : territoires-en-transitions (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des plans et des actions, notamment avec la migration vers tRPC pour plus de performance et de fiabilité. Des améliorations significatives ont également été apportées à l'interface utilisateur, en particulier pour la gestion des référentiels et des indicateurs, avec une attention particulière à la personnalisation et à l'expérience utilisateur. Enfin, des corrections de bugs et des optimisations ont été réalisées pour stabiliser la plateforme et améliorer sa performance globale.

### Évolutions fonctionnelles
- **Plans et Actions :** Migration des mutations de fiche de Supabase vers tRPC pour optimiser les performances et la fiabilité. Possibilité pour les contributeurs pilotes de créer, modifier et supprimer des sous-actions.
- **Rapports :** Ajout de la dernière note dans les rapports et correction du tri des fiches.
- **Référentiels :**
    - Cache des mesures, sous-mesures et tâches désactivées par la personnalisation.
    - Amélioration du message d'alerte pour les mesures affectées par la personnalisation.
    - Recalcule du score courant si la version du référentiel a changé.
- **Indicateurs :** Préserve les favoris et la confidentialité lors d'une mise à jour partielle d'un indicateur.
- **Interface Utilisateur :**
    - Amélioration de l'ergonomie de l'édition de données de l'action (EDL) avec l'utilisation d'un side panel.
    - Ajout de la propriété Badge au composant TabsNext du Design System.
    - Amélioration de l'affichage des titres et de l'organisation des informations sur les pages.
    - Correction de bugs d'affichage et d'interactions.
- **Authentification :** Amélioration de la gestion des erreurs lors de l'inscription.

### Évolutions techniques
- **Architecture :** Migration de certains endpoints SQL vers tRPC pour améliorer les performances et la maintenabilité.
- **Tests :** Amélioration de l'isolation des tests, parallélisation et correction de tests flaky.
- **CI/CD :** Ajout de scripts de backup et restore de la base de données.
- **Infrastructure :** Mise à jour de l'adresse d'envoi d'email.
- **Base de données :** Finalisation de la stratégie de backup & restore.
- **Refactoring :** Suppression de code inutilisé et simplification de certains composants.
- **Déploiement :** Ajout du dashboard privé Streamlit dans le healthcheck.

### Autres changements
- **Documentation :** Mise à jour de la documentation.
- **Configuration :** Ajout de paramètres de configuration pour Claude.
- **Nettoyage de code :** Suppression de fichiers et de code obsolètes.
- **Design System :** Ajout de stories et amélioration des composants Checkbox et TabsNext.
- **Migration :** Script pour modifier les created_at des SA en se basant sur l'ordre des étapes legacy des fiches.
- **Divers :** Mise à jour de la version du spreadsheet.
