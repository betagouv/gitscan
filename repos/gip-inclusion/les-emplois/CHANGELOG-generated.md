## Changelog : les-emplois (30 derniers jours, au 04/10/2026)

### Résumé
Ce mois a été marqué par une évolution majeure de l'identité du service, qui devient "La plateforme de l'inclusion". Au-delà du rebranding, les fonctionnalités de suivi ont été considérablement enrichies, notamment avec un nouveau système complet de gestion des orientations (acceptation, refus, notifications automatiques) et une vue "Synthèse" pour les profils des usagers. La fiabilité et la traçabilité du système ont également été renforcées par la mise en place d'un journal d'audit.

### Évolutions fonctionnelles

**Identité et Interface**
- **Rebranding complet** : Changement de nom du service en "La plateforme de l'inclusion" sur l'ensemble de l'interface, de l'API et de la documentation.
- **Amélioration des profils usagers** : Ajout d'un onglet "Synthèse" (Overview) regroupant les informations clés (derniers accompagnements, candidatures, informations contractuelles).
- **Refonte de l'interface** : Harmonisation des icônes d'organisation, suppression de badges obsolètes et amélioration de l'accessibilité (déclaration de conformité).

**Gestion des Orientations et Accompagnements**
- **Cycle de vie des orientations** : Les prestataires de services peuvent désormais accepter ou refuser une orientation. Le système gère automatiquement l'expiration des orientations et l'envoi de notifications par email aux bénéficiaires et aux émetteurs.
- **Gestion des accompagnements (Assignments)** : Amélioration des outils de gestion pour les professionnels (création, édition, archivage et filtrage des accompagnements).
- **Alertes contractuelles** : Mise en place de compteurs et de bannières pour signaler les fins de contrat imminentes.

**Gestion métier et Administration**
- **Clôture des PASS IAE** : Les employeurs peuvent désormais clôturer un PASS IAE directement via un formulaire interne, avec notification automatique de l'usager.
- **Annuaire Pro** : Ajout de fonctionnalités de géolocalisation des structures dans l'administration et de préférences de visibilité.
- **Gestion des utilisateurs** : Amélioration du processus de désactivation des utilisateurs et possibilité pour un professionnel désactivé de créer un nouveau compte.

**Communications**
- **Emails système** : Amélioration de la qualité des communications avec l'ajout de salutations et le passage au format Markdown pour une meilleure mise en page.

### Évolutions techniques

**Sécurité et Authentification**
- **Intégration ProConnect** : Optimisation du processus d'activation et amélioration de la gestion des clés de sécurité (cache sur les clés JWKS).
- **Traçabilité (Audit Trail)** : Implémentation d'un système de suivi d'audit pour enregistrer les actions et identifier les navigateurs lors des appels de connexion.

**Performance et Architecture**
- **Optimisation du démarrage** : Réduction du temps de résolution d'URL lors de la configuration initiale (gain de 600 ms).
- **Refactoring de la gestion des utilisateurs** : Centralisation de la logique de désactivation pour garantir la cohérence des données.
- **Robustesse des données** : Amélioration de la gestion des fichiers (employee_record) avec des vérifications de noms de fichiers et des mécanismes de verrouillage d'objets lors des uploads.

**Qualité et Tests**
- **Tests automatisés** : Refactoring important de la suite de tests (pytest) et des "factories" pour améliorer la stabilité et la rapidité des tests.
- **Correction de types** : Réduction significative des erreurs de typage (mypy).

### Autres changements
- **Documentation** : Mise à jour de la documentation technique, notamment sur le fonctionnement du SSO et du journal d'audit.
- **Nettoyage** : Suppression de plusieurs commandes de gestion obsolètes et de code non utilisé (notamment les composants liés à DORA).
- **Maintenance** : Correction de nombreuses coquilles, espaces insécables et problèmes d'accents dans l'interface.
