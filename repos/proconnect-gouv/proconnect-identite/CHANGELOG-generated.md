## Changelog : proconnect-identite (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de l'expérience d'authentification (notamment via le MFA), la clarification des communications par email et l'optimisation technique de la récupération des données d'entreprises.

### Évolutions fonctionnelles
- **Amélioration du parcours MFA** : ajout d'un assistant de configuration dans les sections de connexion et de compte, et remplacement du bouton de retour par un bouton de redémarrage du processus MFA ([#2044](https://github.com/proconnect-gouv/proconnect-identite/issues/2044)).
- **Optimisation des communications** : création d'un modèle d'email dédié pour les codes OTP et clarification des messages de vérification d'adresse email ([#2056](https://github.com/proconnect-gouv/proconnect-identite/issues/2056), [#2045](https://github.com/proconnect-gouv/proconnect-identite/issues/2045)).
- **Enrichissement des messages d'erreur** : ajout du numéro SIRET et du libellé de l'entreprise dans les emails d'impossibilité de rejoindre une organisation ([#2073](https://github.com/proconnect-gouv/proconnect-identite/issues/2073)).

### Évolutions techniques
- **Optimisation de la récupération des données** : migration de la source des listes SIREN vers Grist et mise à jour des références de l'Annuaire des Entreprises.
- **Refonte de la logique d'accès** : mise à jour de l'algorithme de jonction de commune et optimisation de la chaîne de vérification des exigences de connexion ([#2059](https://github.com/proconnect-gouv/proconnect-identite/issues/2059), [#2039](https://github.com/proconnect-gouv/proconnect-identite/issues/2039)).
- **Simplification et nettoyage** : suppression du support du scope `organisations` ([#2055](https://github.com/proconnect-gouv/proconnect-identite/issues/2055)), retrait de l'implémentation obsolète `is_service_public` et de l'ancienne méthode de calcul PCI ([#1984](https://github.com/proconnect-gouv/proconnect-identite/issues/1984)).
- **Amélioration de la maintenance** : standardisation des commandes de tests de bout en bout (E2E) ([#2068](https://github.com/proconnect-gouv/proconnect-identite/issues/2068)).

### Autres changements
- **Sécurité** : suppression des directives `unsafe-inline` pour renforcer la politique de sécurité du contenu ([#2026](https://github.com/proconnect-gouv/proconnect-identite/issues/2026)).
