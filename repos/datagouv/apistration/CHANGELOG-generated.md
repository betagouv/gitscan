## Changelog : apistration (30 derniers jours, au 13 octobre 2026)

### Résumé
Ce mois a été marqué par une amélioration majeure de la visibilité et de la compréhension des erreurs pour les développeurs grâce à une nouvelle nomenclature structurée. Le projet a également enrichi ses capacités avec l'intégration de nouveaux flux pour DataPass et une version 3 de l'introspection des jetons. La sécurité a été renforcée par l'imposition du MFA pour ProConnect et une meilleure protection contre les vulnérabilités de type "tabnabbing".

### Évolutions fonctionnelles
- **DataPass** : Introduction de la possibilité de soumettre et de valider des demandes DataPass, ainsi que la consultation de la liste des formulaires associés [#455](https://github.com/datagouv/apistration/pull/455).
- **Nomenclature des erreurs** : Refonte complète de la gestion des codes d'erreur pour les rendre plus explicites, documentés et exposés directement dans les SDKs et sur le portail développeur [#395](https://github.com/datagouv/apistration/pull/395).
- **Introspection de jetons (v3)** : Mise à disposition d'un nouveau point de terminaison d'introspection v3 sur les deux API, accompagné de la régénération des SDK officiels [#415](https://github.com/datagouv/apistration/pull/415).
- **Sécurité des accès** : L'authentification ProConnect exige désormais systématiquement le MFA (authentification multi-facteurs) pour tous les agents [#476](https://github.com/datagouv/apistration/pull/476).
- **Améliorations de l'interface** : 
    - Ajout des logos Data.gouv et Numérique.gouv dans le pied de page [#452](https://github.com/datagouv/apistration/pull/452).
    - Correction du bouton de copie sur la page des liens magiques de jetons publics [#480](https://github.com/datagouv/apistration/pull/480).
    - Amélioration de la lisibilité du tableau de bord (les succès sont désormais affichés en vert) [#444](https://github.com/datagouv/apistration/pull/444).
- **Exports** : Neutralisation des formules dans les exports CSV pour prévenir les injections de données via les tableurs [#484](https://github.com/datagouv/apistration/pull/484).

### Évolutions techniques
- **Résilience des fournisseurs** : 
    - Amélioration de la gestion de l'authentification INSEE (rotation automatique des mots de passe, renouvellement des jetons avant expiration et meilleure gestion des refus) [#383](https://github.com/datagouv/apistration/pull/383), [#477](https://github.com/datagouv/apistration/pull/477).
    - Mise en place de mécanismes de limitation (throttling) pour les introspections FranceConnect [#485](https://github.com/datagouv/apistration/pull/485).
    - Amélioration de la gestion des échecs et des tentatives de reconnexion pour les comptes INPI RNE [#488](https://github.com/datagouv/apistration/pull/488).
- **Sécurité et conformité** :
    - Protection massive contre les attaques par "tabnabbing" sur l'ensemble des liens (administration, site public, Markdown) [#475](https://github.com/datagouv/apistration/pull/475).
    - Renforcement de la sécurité des jetons "éditeur" par l'application stricte des plages d'adresses IP autorisées [#462](https://github.com/datagouv/apistration/pull/462).
    - Filtrage des paramètres sensibles envoyés vers Sentry pour éviter la fuite de données dans les logs d'erreurs [#481](https://github.com/datagouv/apistration/pull/481).
- **Optimisations** : Mise en place de mécanismes de cache pour les dictionnaires DGFIP et pour le statut des points de terminaison (endpoints) [#478](https://github.com/datagouv/apistration/pull/478), [#482](https://github.com/datagouv/apistration/pull/482).
- **CI/CD** : 
    - Intégration de Brakeman dans le pipeline CI pour automatiser la détection de vulnérabilités de sécurité [#471](https://github.com/datagouv/apistration/pull/471).
    - Résolution d'une condition de concurrence (race condition) dans les pipelines de déploiement CI [#412](https://github.com/datagouv/apistration/pull/412).

### Autres changements
- **Documentation** : Mise à jour approfondie de la documentation technique concernant la nomenclature des erreurs, les processus de rotation INSEE et les règles d'accessibilité des liens.
- **Nettoyage** : Suppression de modèles obsolètes (Entreprise) et de tests non utilisés pour alléger la base de code.
