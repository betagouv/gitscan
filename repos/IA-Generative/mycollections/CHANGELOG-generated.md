## Changelog : mycollections (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité de la plateforme, la correction de bugs et l'amélioration de l'expérience utilisateur, notamment au niveau de l'administration et de l'intégration avec OpenRAG. Des améliorations visuelles basées sur le design système DSFR ont également été apportées.

### Évolutions fonctionnelles
- Amélioration du playground : le nombre maximal de tokens a été fixé à 4096 pour les modèles de raisonnement.
- Amélioration du playground : la génération d'évaluations produit désormais des questions une par ligne en cas de fallback.
- Correction d'un bug dans le playground : `/generate-eval` redirige maintenant vers le RAG chat en cas de code 400.
- Séparation des actions utilisateur (création/exploration) des actions d'administration dans l'interface utilisateur.
- Les créateurs de collections conservent désormais l'accès à leurs collections, et le provisioning des groupes lecteurs a été amélioré.
- Les échecs de synchronisation Keycloak vers OpenRAG sont maintenant visibles, avec un client d'administration dédié.
- Les collections sont cloisonnées par groupe Keycloak pour une meilleure sécurité (A01).
- Ajout d'un menu et de routes d'administration réservés aux super-admins.

### Évolutions techniques
- Batterie de tests d'identification et corrections associées (backend pytest + front vitest).
- Mise en place de garde-fous anti-leak pour renforcer la sécurité.
- Configuration de CORS configurable et suppression de la combinaison wildcard+credentials pour une meilleure sécurité.
- Validation des URLs des fetch serveur pour prévenir les attaques SSRF.
- Confinement des chemins dérivés d'entrées utilisateur pour une sécurité accrue.
- Isolation du contenu non fiable inséré dans les prompts LLM et assainissement du rendu HTML du Markdown non fiable côté front.
- Réduction de la divulgation d'informations sur l'endpoint de diagnostic.
- Mise en place d'une authentification JWT sur les routes XHR.

### Autres changements
- Amélioration de l'interface utilisateur avec un logo devant le titre du service et une icône d'application DSFR (collections + graphe de références).
- L'en-tête a été aligné sur le look de myvault, avec le logo en slot opérateur DSFR.
- Checkpoint pris avant les correctifs de sécurité.
