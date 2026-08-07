## Changelog : plusfraichemaville-site (30 derniers jours, au 04/08/2026)

### Résumé
Ce mois-ci, le site a bénéficié de mises à jour de contenus clés, notamment l'intégration du budget 2025 et l'actualisation des données climatiques. Un travail important a également été réalisé pour améliorer le référencement naturel (SEO) du site et permettre une meilleure interopérabilité des données via de nouvelles interfaces de programmation (API).

### Évolutions fonctionnelles
- **Mise à jour des données climatiques** : Actualisation des données relatives aux zones climatiques locales (LCZ) et amélioration de la clarté des informations via une modification du texte et de la fenêtre modale [#521](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/521).
- **Nouveaux contenus** : Ajout des informations concernant le budget 2025 [#519](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/519).
- **Simplification de l'interface** : Suppression des sections sur les aides régionales et des liens vers les aides territoriales sur les fiches solutions pour épurer l'expérience utilisateur [#517](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/517).
- **Correction de contenu** : Rectification d'une coquille sur la page dédiée aux risques sanitaires.

### Évolutions techniques
- **Optimisation du référencement (SEO)** : 
    - Mise en place de liens canoniques pour les pages de retours d'expérience (REX) et le site en général [#516](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/516).
    - Ajout de métadonnées spécifiques pour les pages REX [#515](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/515).
    - Nettoyage automatique des balises HTML dans les méta-descriptions pour un affichage propre dans les moteurs de recherche.
- **Interopérabilité et gestion des données** :
    - Création d'une nouvelle route API permettant au projet PFAT de consommer les données Climadiag [#520](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/520).
    - Amélioration du processus de mise à jour des données Climadiag pour éviter l'écrasement accidentel des données LCZ.
- **Analyse et suivi** : Intégration de nouveaux événements et tags Matomo pour affiner le suivi des comportements utilisateurs [#518](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/518).
- **Fiabilité** : Correction d'un bug de validation pour empêcher l'envoi de chaînes de caractères vides.
