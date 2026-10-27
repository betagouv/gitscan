## Changelog : menshen (30 derniers jours, au 25 octobre 2026)

### Résumé
Cette période est marquée par le passage à la version 0.4.0. Les évolutions majeures concernent la restructuration du format des portées (scopes) de jetons pour une gestion plus granulaire des permissions, ainsi qu'un renforcement significatif de l'environnement de test et de la robustesse de l'infrastructure.

### Évolutions fonctionnelles
- **Gestion des permissions** : Évolution du modèle de définition des portées (scopes) de jetons vers un format standardisé `service:resource:action`.

### Évolutions techniques
- **Tests et environnement de démonstration (Playground)** :
    - Mise en place de tests de bout en bout (E2E) pour Keycloak et l'environnement de playground.
    - Intégration du client Menshen et ajout de nouvelles configurations (audience mapper, variante ProConnect).
- **Infrastructure et CI/CD** :
    - Optimisation des workflows GitHub Actions (mise à jour de `setup-uv` et adoption des presets CI de la suite numérique).
    - Amélioration de la sécurité en supprimant le certificat racine emSign des dépendances.
- **Backend et Client** :
    - Amélioration de la gestion des logs via l'intégration de la configuration `lasuite`.
    - Ajout d'un délai d'attente (timeout) par défaut pour les requêtes POST dans le client.
    - Mise à jour de la dépendance `django-lasuite`.
    - Nettoyage de l'interface d'administration (suppression de propriétés inconnues).

### Autres changements
- **Qualité du code** : Configuration et résolution des avertissements du linter, et correction de fautes de frappe dans les messages de log.
