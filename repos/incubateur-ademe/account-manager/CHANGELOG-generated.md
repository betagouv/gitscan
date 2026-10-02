## Changelog : account-manager (30 derniers jours, au 01/10/2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes dans la gestion des droits Scalingo et l'intégration des comptes machines. L'expérience utilisateur a été enrichie par une meilleure visibilité sur le statut des actions et une gestion plus fluide des dérogations et des transferts, tout en renforçant la fiabilité globale via une suite de tests plus robuste.

### Évolutions fonctionnelles
- **Gestion Scalingo** : Administration des droits [#107], couverture des collaborateurs [#101] et optimisation de la collecte des données pour éviter les expirations [#102].
- **Comptes machines** : Possibilité de déclarer une machine depuis la file des comptes isolés [#105] et de la rattacher directement au système concerné [#106].
- **Expérience utilisateur et visibilité** : 
    - Affichage des comptes dans l'espace personnel de l'utilisateur [#120].
    - Suivi précis du statut des gestes (confirmé, en cours ou soldé) sur les fiches [#136] et visibilité des plans en attente de confirmation [#129].
    - Améliorations de l'interface : maintien de la saisie après un refus de formulaire [#144], correction de l'alignement des textes [#137] et clarification des liens d'accès [#82].
- **Workflows et automatisation** : 
    - Gestion des dérogations (pose et levée) directement depuis les constats [#94].
    - Retrait automatique d'un compte d'une organisation GitHub [#145].
    - Sécurisation des transferts (exigence d'un repreneur pour les transferts Scalingo [#134] et gestion du transfert de propriété des applications [#125]).
- **Alerting et contrôle** : Signalement des modèles de départ non relus [#122], gestion des tolérances par cible [#114] et alertes en cas de risque de coupure [#98].

### Évolutions techniques
- **Tests** : Renforcement significatif de la fiabilité de la suite de tests, notamment pour la vérification visuelle des écrans [#116] et la gestion des scénarios multi-étages [#83].
- **Infrastructure et Build** : Mise à jour de Next.js [#85] et des dépendances de build (Nodemailer, Vitest, Fast-uri) [#87].
- **Architecture et Logique** : 
    - Uniformisation du vocabulaire utilisé dans les écrans [#84].
    - Standardisation de la gestion des dates au fuseau horaire de Paris [#133].
    - Refactorisation de l'affichage des étapes de plans dans les dossiers [#126].

### Autres changements
- **Documentation** : Mise à jour des documents d'architecture concernant les changements de l'administration Scalingo [#62], la configuration à trois niveaux [#6e] et les nouveaux connecteurs [#25].
- **Processus** : Intégration de la demande d'amendements d'architecture directement lors du traitement des tickets.
