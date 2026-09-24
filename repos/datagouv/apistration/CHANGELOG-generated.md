## Changelog : apistration (30 derniers jours, au 23 septembre 2026)

### Résumé
Ce mois-ci, apistration a franchi des étapes importantes avec le lancement des ressources pour les associations (incluant la sortie du SDK 0.4.0), l'introduction de preuves d'attestation pour l'EAJE, et une amélioration majeure de la clarté des erreurs pour les développeurs utilisant les services INSEE et CNAV.

### Évolutions fonctionnelles
- **Associations** : Ajout de nouveaux points de terminaison (MI/SIAF), mise à jour du catalogue et publication des SDK 0.4.0. [#384](https://github.com/datagouv/apistration/pull/384)
- **EAJE** : Mise en place de la gestion des preuves d'attestation, incluant la génération de PDF vérifiables, l'utilisation de jetons chiffrés et la possibilité de demander une preuve via un en-tête HTTP. [#432](https://github.com/datagouv/apistration/pull/432)
- **Transparence des erreurs** : 
    - Amélioration du détail des refus d'authentification INSEE pour identifier précisément le motif de l'échec. [#429](https://github.com/datagouv/apistration/pull/429)
    - Meilleure catégorisation des erreurs 400 de la CNAV par code d'erreur fournisseur. [#401](https://github.com/datagouv/apistration/pull/401)
- **Administration & Back-office** : 
    - Affichage des réponses brutes des fournisseurs pour faciliter le débogage. [#397](https://github.com/datagouv/apistration/pull/397)
    - Suivi des changements d'adhésion des éditeurs dans les activités d'administration. [#379](https://github.com/datagouv/apistration/pull/379)
    - Amélioration de l'interface de requêtes manuelles (support des en-têtes OpenAPI et listes déroulantes pour les énumérations). [#410](https://github.com/datagouv/apistration/pull/410)
- **Expérience utilisateur** : Mise à jour de la terminologie pour plus de clarté (ex: passage de "nom de naissance" à "nom de famille"). [#362](https://github.com/datagouv/apistration/pull/362)

### Évolutions techniques
- **CI/CD** : Optimisation des workflows GitHub Actions, notamment via la variabilisation des cibles de déploiement et la résolution de problèmes de concurrence lors des merges. [#437](https://github.com/datagouv/apistration/pull/437), [#412](https://github.com/datagouv/apistration/pull/412)
- **Gestion des erreurs et logs** : 
    - Introduction de sous-codes d'erreur dans les logs d'accès pour un meilleur diagnostic. [#380](https://github.com/datagouv/apistration/pull/380)
    - Amélioration de la gestion des erreurs de handshake TLS (conversion en erreur 502 propre). [#363](https://github.com/datagouv/apistration/pull/363)
- **Sécurité** : 
    - Automatisation de la rotation des mots de passe INSEE. [#383](https://github.com/datagouv/apistration/pull/383)
    - Mise en place de la révocation en cascade des habilitations sur leurs délégations respectives. [#397](https://github.com/datagouv/apistration/pull/397)
- **Refactoring** : Nettoyage du code et suppression d'exemples de tests HTTP inutilisés. [#426](https://github.com/datagouv/apistration/pull/426)

### Autres changements
- **Documentation** : Enrichissement des documentations techniques concernant l'authentification INSEE, les règles de l'API-SECU, les régimes de formation MESRI et le dictionnaire DGFiP. [#402](https://github.com/datagouv/apistration/pull/402), [#411](https://github.com/datagouv/apistration/pull/411)
- **Configuration** : Ajustement du fichier `robots.txt` pour interdire l'indexation des environnements hors production. [#399](https://github.com/datagouv/apistration/pull/399)
