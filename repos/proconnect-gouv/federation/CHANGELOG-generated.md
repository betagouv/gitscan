## Changelog : federation (30 derniers jours, au 2026-09-11)

### Résumé
Les récentes évolutions renforcent la fiabilité de la plateforme face aux indisponibilités de services tiers (API Entreprise, SIRENE) grâce à l'ajout de mécanismes de secours et d'une meilleure gestion des erreurs. Le projet a également bénéficié d'un nettoyage technique important et d'une optimisation de l'environnement de développement.

### Évolutions fonctionnelles
- **Résilience accrue** : mise en place d'un système de secours (fallback) utilisant des données en cache lorsque l'API Entreprise est indisponible [#1549](https://github.com/proconnect-gouv/federation/issues/1549).
- **Amélioration de l'expérience utilisateur** : les erreurs liées aux services externes (SIRENE, Grist) sont désormais mieux exposées et gérées pour informer l'utilisateur [#1577](https://github.com/proconnect-gouv/federation/issues/1577).
- **Corrections de bugs** : 
    - Résolution d'un problème de navigation (bouton retour) causé par les restrictions de sécurité CSP [#1544](https://github.com/proconnect-gouv/federation/issues/1544).
    - Correction du calcul du compte à rebours pour les emails [#1528](https://github.com/proconnect-gouv/federation/issues/1528).

### Évolutions techniques
- **Sécurité** : adoption de l'algorithme RS256 par défaut pour la sélection des algorithmes de réponse signée [#1548](https://github.com/proconnect-gouv/federation/issues/1548).
- **Infrastructure & Docker** : optimisation de la construction de l'image Docker du backend pour inclure les assets et le CSS [#1529](https://github.com/proconnect-gouv/federation/issues/1529).
- **Refactoring** : 
    - Simplification des exceptions en supprimant le préfixe `CoreFca` [#1545](https://github.com/proconnect-gouv/federation/issues/1545).
    - Ajout de dossiers de vues manquants [#1527](https://github.com/proconnect-gouv/federation/issues/1527).
- **Environnement de développement** : refonte du processus de seeding et des migrations pour la stack de développement locale [#1455](https://github.com/proconnect-gouv/federation/issues/1455).
- **CI/CD & Observabilité** : 
    - Correction des erreurs de communication avec Grist lors des tests automatisés en CI [#1546](https://github.com/proconnect-gouv/federation/issues/1546).
    - Ajout de logs pour le suivi des mises à jour Grist [#1551](https://github.com/proconnect-gouv/federation/issues/1551).
- **Maintenance** : mise à jour des packages internes `@proconnect-gouv` [#1585](https://github.com/proconnect-gouv/federation/issues/1585).

### Autres changements
- **Nettoyage** : suppression de plusieurs packages inutilisés pour alléger le projet [#1590](https://github.com/proconnect-gouv/federation/issues/1590).
- **Documentation** : réécriture et clarification de certains éléments du code [#1550](https://github.com/proconnect-gouv/federation/issues/1550).
