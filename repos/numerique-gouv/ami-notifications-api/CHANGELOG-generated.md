## Changelog : ami-notifications-api (30 derniers jours, au 02 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment sur les pages de suivi et d'agenda, ainsi que par l'implémentation de la gestion des notifications archivées. Des travaux ont également été réalisés pour préparer l'intégration avec le service FranceConnect et améliorer la robustesse de la réplication des données.

### Évolutions fonctionnelles
- **Suivi des demandes (FollowUp):**
    - Ajout de la possibilité d'archiver les demandes de suivi.
    - Page dédiée pour consulter les demandes archivées.
    - Simplification de l'interface de suivi, suppression des onglets.
    - Ajout d'un indicateur visuel pour les demandes archivées.
- **Notifications:**
    - Amélioration de l'affichage des icônes de notification, avec récupération depuis l'item associé ou utilisation d'une icône par défaut.
    - Exclusion des notifications expirées lors de la récupération en liste.
    - Ajout d'un champ `valid_until` pour gérer la durée de validité des notifications.
- **FranceConnect (FI):**
    - Implémentation d'une vue pour l'authentification silencieuse via FranceConnect.
    - Ajout d'une page intermédiaire pour gérer le processus d'authentification FI.
    - Possibilité de choisir le fournisseur d'authentification FranceConnect.
    - Affichage des données de l'utilisateur après authentification FI.
- **Adresse:** Correction d'un bug d'affichage sur la page d'édition d'adresse.

### Évolutions techniques
- **API:**
    - Ajout du champ `item_is_archived` au modèle de notification.
    - Modification de l'API pour exposer les champs `external_item_type` et `external_item_id` pour les suivis.
    - Implémentation d'un nouveau point de terminaison pour archiver un item de suivi.
    - Refactorisation de l'API pour gérer les notifications expirées.
- **Infrastructure:**
    - Mise à jour des dépendances : `ujson`, `msgpack`, `pyjwt`, `webob`, `cryptography`, `esbuild`, `@sveltejs/vite-plugin-svelte`, `vite`, `@vitejs/plugin-basic-ssl`, `dompurify`, `js-yaml`.
    - Utilisation de `django-tasks-db` par défaut pour la gestion des tâches asynchrones.
    - Ajout de tests pour la page de préférences de zone.
- **Réplication:**
    - Prise en compte du champ `subscription` lors de la réplication des enregistrements.

### Autres changements
- Amélioration de la conformité RGAA (accessibilité) sur plusieurs composants de l'interface utilisateur.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour de la documentation.
- Suppression de code obsolète.
- Amélioration des performances de la récupération de la liste des notifications.
- Ajout de métriques pour suivre le nombre de notifications envoyées.
- Correction d'un problème de déconnexion inattendue avec FranceConnect.
- Ajout d'un meta tag pour la sécurité (referrer).
- Correction de l'affichage de la hauteur de la page en mode mobile.
- Suppression de code inutile sur la page d'agenda.
- Renommage de certaines librairies et routes pour plus de cohérence (agenda, followup, requests).
