## Changelog : referentiel-applications (30 derniers jours, au 21 août 2026)

### Résumé
Cette période a été marquée par l'introduction d'un moteur de détection de corrélations entre applications et un renforcement significatif des outils d'administration et de sécurité (gestion des utilisateurs, traçabilité accrue). L'expérience utilisateur a également été affinée avec l'ajout de filtres sauvegardés et une amélioration de l'accessibilité, tandis que l'infrastructure a bénéficié d'une mise à jour majeure vers NestJS 11.

### Évolutions fonctionnelles
- **Moteur de corrélation** : Mise en place d'un moteur de détection de corrélations avec scoring et tâches planifiées, incluant la gestion des suggestions (liste, acceptation et rejet) [#2318](https://github.com/dnum-mi/referentiel-applications/issues/2318), [#2319](https://github.com/dnum-mi/referentiel-applications/issues/2319), [#2324](https://github.com/dnum-mi/referentiel-applications/issues/2324).
- **Administration et Sécurité** : 
    - Possibilité pour les administrateurs de bannir des utilisateurs [#2240](https://github.com/dnum-mi/referentiel-applications/issues/2240).
    - Gestion des directions métier et des rattachements aux organisations [#2218](https://github.com/dnum-mi/referentiel-applications/issues/2218).
    - Sécurisation de l'impersonation : restriction au périmètre de l'administrateur local et traçabilité de l'administrateur réel lors des modifications [#2221](https://github.com/dnum-mi/referentiel-applications/issues/2221), [#2227](https://github.com/dnum-mi/referentiel-applications/issues/2227).
    - Mise en place d'un mode maintenance en lecture seule [#2201](https://github.com/dnum-mi/referentiel-applications/issues/2201).
- **Expérience Utilisateur (UX/UI)** :
    - Ajout de filtres sauvegardés pour les applications [#2309](https://github.com/dnum-mi/referentiel-applications/issues/2309).
    - Amélioration de l'accessibilité (score RGAA) [#2181](https://github.com/dnum-mi/referentiel-applications/issues/2181).
    - Ajout d'info-bulles sur les cartes de dette technique [#2220](https://github.com/dnum-mi/referentiel-applications/issues/2220) et de nouveaux éléments visuels (CTA IQ, espacements, états de chargement) [#2325](https://github.com/dnum-mi/referentiel-applications/issues/2325), [#2124](https://github.com/dnum-mi/referentiel-applications/issues/2124), [#2155](https://github.com/dnum-mi/referentiel-applications/issues/2155).
- **Gouvernance des données** : 
    - Amélioration de la vérification des dates de fin de vie (EOL) des technologies [#2234](https://github.com/dnum-mi/referentiel-applications/issues/2234).
    - Normalisation des tags et des entrées de stacks technologiques (insensibilité à la casse) [#2202](https://github.com/dnum-mi/referentiel-applications/issues/2202), [#2317](https://github.com/dnum-mi/referentiel-applications/issues/2317).

### Évolutions techniques
- **Architecture et Backend** : 
    - Migration majeure vers NestJS 11 [#2153](https://github.com/dnum-mi/referentiel-applications/issues/2153).
    - Centralisation des vérifications de permissions côté frontend via un hook dédié [#2245](https://github.com/dnum-mi/referentiel-applications/issues/2245).
    - Refactoring du backend pour la déduplication du code et l'unification des labels (statuts et types de relations) entre le backend et le frontend [#2250](https://github.com/dnum-mi/referentiel-applications/issues/2250), [#2246](https://github.com/dnum-mi/referentiel-applications/issues/2246).
- **Modèle de données** : Introduction de nouveaux modèles et types de relations pour supporter la détection de corrélation [#2323](https://github.com/dnum-mi/referentiel-applications/issues/2323).
- **Qualité et Tests** : 
    - Amélioration de l'isolation des tests pour éviter la pollution de la base de données de développement [#2117](https://github.com/dnum-mi/referentiel-applications/issues/2117).
    - Correction de vulnérabilités et de problèmes de qualité de code (XSS, types "any") [#2275](https://github.com/dnum-mi/referentiel-applications/issues/2275).

### Autres changements
- Mise à jour de la documentation du projet [#2239](https://github.com/dnum-mi/referentiel-applications/issues/2239).
