## Changelog : a-just (30 derniers jours, au 02 juin 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'interface utilisateur, notamment sur les pages Panorama et Cockpit, avec l'ajout d'aide contextuelle et de tests automatisés pour garantir la stabilité. Des corrections ont également été apportées pour améliorer la précision des données affichées et la gestion des simulations. Enfin, des efforts ont été consentis pour améliorer la robustesse et la sécurité de l'application.

### Évolutions fonctionnelles
- Ajout d'un bouton "Qu'est-ce que c'est ?" pour les utilisateurs n'ayant pas les droits de modification des ressources humaines sur le ventilateur des ressources humaines.
- Amélioration de l'aide contextuelle (IntroJS) sur les pages Panorama et Cockpit pour guider les utilisateurs.
- Correction d'un bug empêchant l'affichage correct des contentieux après la complétion des données.
- Amélioration de l'affichage des agents dans les colonnes "Arrivées" et "Départs" des changements d'effectifs.
- Ajout d'un test E2E pour vérifier la disponibilité des données sur le Panorama.
- Possibilité de modifier la date de début des simulations.
- Correction de l'affichage des catégories d'agents dans le simulateur.
- Ajout d'alertes et d'informations sur les erreurs dans les graphiques du Cockpit.
- Amélioration de la gestion des congés et des absences (ASA).

### Évolutions techniques
- Mise à jour de la méthode d'accès aux variables d'environnement dans les tests E2E, utilisant `cy.env` et `SANDBOX_API_URL`.
- Correction de la configuration de Redis en Docker pour assurer un redémarrage automatique.
- Refonte de l'accès aux variables d'environnement dans les tests E2E pour une meilleure gestion et sécurité.
- Mise à jour des dépendances, notamment `@emnapi` et `esbuild`.
- Amélioration de la robustesse des tests E2E avec l'ajout de `cy.wait()` pour synchroniser les actions.
- Correction de bugs et amélioration du code dans divers composants, notamment le cockpit et le simulateur.
- Migration des règles ASA vers la gestion des absences.

### Autres changements
- Ajout de fichiers `.env.example` pour faciliter la configuration des tests E2E.
- Amélioration des logs pour faciliter le débogage.
- Corrections de fautes de frappe et amélioration de la lisibilité du code.
- Suppression de code inutilisé.
- Mise à jour de la version de l'application.
