## Changelog : proconnect-identite (30 derniers jours, au 12/08/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience utilisateur lors de l'authentification, notamment via l'ajout d'un assistant pour la double authentification (MFA). Le projet a également bénéficié d'une clarification importante des communications par e-mail et de plusieurs optimisations techniques visant à simplifier le code et à renforcer la sécurité.

### Évolutions fonctionnelles
- **Amélioration du parcours MFA** : Intégration d'un assistant dédié pour la double authentification dans les sections de connexion et de gestion du compte, incluant un bouton de redémarrage du processus [#2044](https://github.com/proconnect-gouv/proconnect-identite/pull/2044).
- **Optimisation des communications e-mail** : 
    - Création d'un modèle d'e-mail dédié pour les codes OTP [#2066](https://github.com/proconnect-gouv/proconnect-identite/pull/2066).
    - Ajout du numéro SIRET et du libellé de l'organisation dans les e-mails d'échec d'adhésion pour une meilleure clarté [#2073](https://github.com/proconnect-gouv/proconnect-identite/pull/2073).
    - Amélioration de la rédaction et correction de fautes de frappe sur les pages et modèles de vérification d'e-mail [#2056](https://github.com/proconnect-gouv/proconnect-identite/pull/2056) [#2045](https://github.com/proconnect-gouv/proconnect-identite/pull/2045).
- **Corrections d'interface** : Résolution d'une erreur de syntaxe sur la page de vérification d'e-mail [#2048](https://github.com/proconnect-gouv/proconnect-identite/pull/2048).
- **Gestion des accès** : Suppression du support du scope `organisations`.

### Évolutions techniques
- **Sécurité et Refactoring** :
    - Suppression de l'implémentation obsolète `is_service_public`.
    - Renforcement de la sécurité par la suppression des directives `unsafe-inline` [#2026](https://github.com/proconnect-gouv/proconnect-identite/pull/2026).
    - Refactorisation de la gestion des gardes de connexion (`userSignInRequirementsGuard`) pour un traitement récursif.
    - Suppression d'un ancien calcul PCI.
- **Algorithmes et Données** : Mise à jour de l'algorithme de jonction des communes.
- **Tests et Qualité** :
    - Standardisation des commandes de tests de bout en bout (E2E).
    - Mise à jour des fixtures de l'annuaire pour les synchroniser avec les données réelles de l'API [#2035](https://github.com/proconnect-gouv/proconnect-identite/pull/2035).
    - Ajout de tests pour l'assistant MFA.
- **Optimisation des templates** : Nettoyage des modèles d'e-mails par la suppression de paramètres inutilisés (`baseurl`).

### Autres changements
- Automatisation du versionnage et de la publication des packages via Changesets.
