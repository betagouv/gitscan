## Changelog : federation (30 derniers jours, au 19 août 2026)

### Résumé
Ce mois a été marqué par une restructuration importante de l'architecture pour gagner en modularité, ainsi que par une amélioration significative de la sécurité et de l'expérience utilisateur autour de la vérification d'identité et du MFA (authentification multi-facteurs). Le projet est devenu plus robuste grâce à une meilleure gestion des erreurs et une séparation plus nette des composants de test et de simulation.

### Évolutions fonctionnelles
- **Amélioration de la vérification par email** : Clarification des messages et des sujets d'emails [#1425, #855942c], utilisation de templates dédiés avec des codes OTP plus courts pour plus de fluidité [#1477], et contrôle strict des renvois d'emails de vérification [#1458].
- **Renforcement de la sécurité MFA** : Introduction d'un mode de secours (fallback) par email pour les fournisseurs d'identité ne supportant pas le MFA, et optimisation de la réutilisation des sessions MFA pour répondre aux exigences de sécurité (ACR) [#1450].
- **Interface et API** : Renommage de "Fournisseur de données" en "Serveur de ressources" pour plus de clarté, blocage par défaut des emails de domaine lors de la création d'un fournisseur d'identité en administration [#1476], et ajout d'une capacité de suppression des clients OIDC via l'API [#1390].

### Évolutions techniques
- **Modularisation de l'architecture** : Extraction de plusieurs composants (notamment `csmr-rie`, `mock-data-provider` et les différents fournisseurs de services de mock) en applications autonomes pour simplifier la maintenance [#1428, #1424, #1416, #1413].
- **Refactoring et nettoyage du code** : Migration de la gestion des erreurs vers les filtres d'exception NestJS, renommage technique de `fqdn` en `attachedEmailDomain` [#1485], et suppression des références et des méthodes de chiffrement obsolètes pour les serveurs de ressources.
- **Optimisation des bases de données** : Refonte du processus de peuplement (seeding) de l'environnement de développement [#1455], exécution des migrations via un hook de démarrage plutôt qu'à l'initialisation [#1453], et correction des migrations liées aux domaines d'emails [#1508].
- **DevOps et Qualité** : Simplification des builds Docker multi-étapes [#1452], ajout de points de contrôle de santé (healthchecks) pour l'administration [#1391], et optimisation des commandes de tests E2E.

### Autres changements
- **Documentation** : Mise à jour de la description du README [#1448] et ajout de documentation spécifique pour hyyyperbridge.
- **Nettoyage** : Suppression de fonctions et de tests non utilisés pour alléger la base de code.
