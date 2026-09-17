## Changelog : mon-indemnisation-justice (30 derniers jours, au 16 septembre 2026)

### Résumé
Cette période a été marquée par une amélioration significative de la gestion documentaire (génération de PDF, nouveaux formulaires) et de l'expérience de clôture des dossiers. Parallèlement, une refonte technique majeure a permis de simplifier l'application en déplaçant la logique métier vers le serveur et en modernisant l'ensemble de l'environnement technologique.

### Évolutions fonctionnelles
- **Gestion des dossiers et clôture** : 
    - Introduction d'une nouvelle interface (modale) pour la clôture des dossiers, incluant la saisie de motifs et d'explications.
    - Possibilité pour les agents de la PN de s'affecter directement à un bâtiment de la PP.
    - Amélioration du système de notifications (envoi à la DA et à la FIP3) [\#175](https://github.com/betagouv/mon-indemnisation-justice/pull/175).
- **Documents et impressions** :
    - Amélioration de la génération de PDF : conversion automatique des documents requis, gestion des fichiers incompatibles et export FIP3 en PDF [\#170](https://github.com/betagouv/mon-indemnisation-justice/pull/170).
    - Utilisation des codes départements (ex: 2A, 976) dans les courriers officiels.
    - Amélioration de la prévisualisation des fichiers signés et correction des problèmes d'affichage de PDF sur le navigateur Edge.
    - Mise en place d'un système de détection et de remontée d'erreurs lors de l'impression [\#162](https://github.com/betagouv/mon-indemnisation-justice/pull/162).
- **Formulaires** : Mise en place de nouveaux formulaires de déclaration et de téléversement de la DA [\#169](https://github.com/betagouv/mon-indemnisation-justice/pull/169).
- **Corrections** : 
    - Résolution de problèmes de doublons lors de l'affectation [\#163](https://github.com/betagouv/mon-indemnisation-justice/pull/163).
    - Correction de bugs liés aux dates de marquage d'indemnisation et aux décalages de données entre le frontend et le backend.

### Évolutions techniques
- **Refonte de l'architecture frontend** : Simplification majeure du code par la suppression de librairies de gestion d'état (MobX, Valtio) et de date-fns, en déléguant davantage de logique métier vers l'API.
- **Modernisation de la stack** : Montée de version globale des composants critiques : PHP 8.5, Symfony 8.1, Node 24 et mise à jour des GitHub Actions.
- **Fiabilisation de la génération de documents** : Migration vers l'utilisation de Firefox via Puppeteer pour assurer une meilleure stabilité des rendus PDF [\#166](https://github.com/betagouv/mon-indemnisation-justice/pull/166).
- **Optimisations et tests** : 
    - Amélioration des performances en optimisant les mécanismes de tentatives (retries) et la gestion du cache.
    - Renforcement de la couverture de tests avec l'ajout de nouveaux tests unitaires.

### Autres changements
- Mise à jour de la documentation technique.
