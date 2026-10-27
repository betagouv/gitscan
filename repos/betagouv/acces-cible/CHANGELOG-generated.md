## Changelog : acces-cible (30 derniers jours, au 26/10/2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de la précision des audits d'accessibilité et l'optimisation de l'expérience utilisateur. Les utilisateurs bénéficient de nouveaux outils de filtrage et d'un meilleur suivi de l'avancement des tâches, tandis que l'infrastructure technique a été modernisée avec des mises à jour de Ruby et Rails pour garantir une meilleure stabilité.

### Évolutions fonctionnelles
- **Amélioration de la détection** : Optimisation de la détection du taux de conformité et de la flexibilité des expressions régulières pour identifier les mentions d'accessibilité [#751](https://github.com/betagouv/acces-cible/issues/751), [#789](https://github.com/betagouv/acces-cible/issues/789), [#790](https://github.com/betagouv/acces-cible/issues/790) et [#774](https://github.com/betagouv/acces-cible/issues/774).
- **Nouveaux outils de suivi** : Ajout d'un filtre pour afficher le dernier audit par site [#777](https://github.com/betagouv/acces-cible/issues/777) et mise en place d'un indicateur de progression pour les lots d'audits [#739](https://github.com/betagouv/acces-cible/issues/739).
- **Interface utilisateur (UI)** : 
    - Nouveau design pour les appels à la redirection [#762](https://github.com/betagouv/acces-cible/issues/762).
    - Ajout de cartes cliquables pour faciliter la navigation [#737](https://github.com/betagouv/acces-cible/issues/737).
    - Ajustements ergonomiques de la page d'accueil [#734](https://github.com/betagouv/acces-cible/issues/734) et redirection automatique vers l'accueil après déconnexion [#733](https://github.com/betagouv/acces-cible/issues/733).
- **Analyse** : Ajustements de l'analyse des dates de loi et des schémas de données [#759](https://github.com/betagouv/acces-cible/issues/759).

### Évolutions techniques
- **Mises à jour majeures** : Passage à Ruby 4.0.7 [#791](https://github.com/betagouv/acces-cible/issues/791) et régénération des schémas pour Rails 8.1.4 [#752](https://github.com/betagouv/acces-cible/issues/752).
- **Capacités d'audit** : 
    - Amélioration de l'extraction de contenu (support des "shadowroots") pour une analyse plus profonde [#785](https://github.com/betagouv/acces-cible/issues/785).
    - Résolution de problèmes de chargement (CSS et Google API) impactant les sites de type SPA [#794](https://github.com/betagouv/acces-cible/issues/794).
- **Optimisations et stabilité** : 
    - Refactorisation du service de création de lots d'audits [#748](https://github.com/betagouv/acces-cible/issues/748).
    - Correction d'une condition de concurrence (race condition) sur le compteur de progression des lots [#738](https://github.com/betagouv/acces-cible/issues/738).
    - Optimisation des mises à jour en temps réel via `broadcast_update_to` [#735](https://github.com/betagouv/acces-cible/issues/735).
- **Observabilité et sécurité** : 
    - Amélioration de la configuration de Sentry et du filtrage des logs [#756](https://github.com/betagouv/acces-cible/issues/756), [#754](https://github.com/betagouv/acces-cible/issues/754).
    - Renforcement de la sécurité et de la configuration de l'environnement de staging [#771](https://github.com/betagouv/acces-cible/issues/771), [#763](https://github.com/betagouv/acces-cible/issues/763).

### Autres changements
- Mise à jour des traductions [#769](https://github.com/betagouv/acces-cible/issues/769).
- Publication de la version 3.0.0 [#691](https://github.com/betagouv/acces-cible/issues/691).
